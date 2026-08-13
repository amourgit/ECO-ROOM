"""
CivitasBrowser — Chrome headless participant Jitsi.

Responsabilités UNIQUEMENT :
  1. Rejoindre la room Jitsi
  2. Capturer les événements Jitsi via expose_function __civitasEvent
  3. Gérer l'audio entrant (tracks distants → AudioPipe Python)
  4. Gérer l'audio sortant (Gemini → replaceTrack dans JVB)
  5. Envoyer des messages chat

Ce module ne contient AUCUNE logique métier.
Toute la logique est dans EventBus + handlers + instance.py.
"""
import asyncio
import logging
from playwright.async_api import async_playwright, Page, Browser, BrowserContext

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# RTC SPY — intercepte setLocalDescription pour le replaceTrack audio sortant
# Injecté EN PREMIER avant tout, pour intercepter la négociation SDP initiale
# ─────────────────────────────────────────────────────────────────────────────
RTC_SPY_JS = """
() => {
  if (window._civitasRtcSpy) return 'already';
  window._civitasRtcSpy = true;

  const Orig = window.RTCPeerConnection;
  window.RTCPeerConnection = function(...args) {
    const pc = new Orig(...args);
    const origSLD = pc.setLocalDescription.bind(pc);

    pc.setLocalDescription = async function(desc) {
      const r = await origSLD(desc);
      // Double tentative : immédiat + différé pour couvrir tous les timings
      [200, 1000, 3000, 6000].forEach(delay => setTimeout(() => {
        const outTrack = window._civitasOutStream?.getAudioTracks()[0];
        if (!outTrack) return;
        const sender = pc.getSenders().find(s => s.track?.kind === 'audio');
        if (sender && sender.track !== outTrack) {
          sender.replaceTrack(outTrack)
            .then(() => console.log('[CIVITAS] replaceTrack OK @' + delay + 'ms'))
            .catch(e => console.warn('[CIVITAS] replaceTrack err:', e.message));
        }
      }, delay));
      return r;
    };
    return pc;
  };
  window.RTCPeerConnection.prototype = Orig.prototype;
  console.log('[CIVITAS] RTC spy ✓');
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# AUDIO BRIDGE
#
# Entrant  : tracks distants via TRACK_ADDED (lib-jitsi-meet) → PCM 16kHz → WS
# Sortant  : PCM 24kHz ← WS → AudioContext → MediaStreamDestination → replaceTrack
# Fallback : éléments <audio> DOM si _room inaccessible
# ─────────────────────────────────────────────────────────────────────────────
AUDIO_BRIDGE_JS = """
(async (wsPort) => {
  if (window._civitasAudioBridge) return 'already_running';
  window._civitasAudioBridge = true;

  // ── WebSocket Python ─────────────────────────────────────────────────────
  const ws = new WebSocket(`ws://127.0.0.1:${wsPort}`);
  ws.binaryType = 'arraybuffer';
  window._civitasWS = ws;

  await new Promise((res, rej) => {
    ws.onopen  = res;
    ws.onerror = () => rej(new Error('WS failed'));
    setTimeout(() => rej(new Error('WS timeout')), 5000);
  });

  // ── Entrant 16kHz → Gemini ───────────────────────────────────────────────
  const inCtx = new AudioContext({ sampleRate: 16000 });
  window._civitasInCtx = inCtx;

  await inCtx.audioWorklet.addModule(
    'data:application/javascript,' + encodeURIComponent(`
      class PCMSender extends AudioWorkletProcessor {
        process(inputs) {
          const ch = inputs[0]?.[0];
          if (ch?.length > 0) {
            const pcm = new Int16Array(ch.length);
            for (let i = 0; i < ch.length; i++)
              pcm[i] = Math.max(-32768, Math.min(32767, ch[i] * 32768));
            this.port.postMessage(pcm.buffer, [pcm.buffer]);
          }
          return true;
        }
      }
      registerProcessor('pcm-sender', PCMSender);
    `)
  );

  const worklet = new AudioWorkletNode(inCtx, 'pcm-sender');
  worklet.port.onmessage = (e) => {
    if (ws.readyState === WebSocket.OPEN) ws.send(e.data);
  };

  const merger = inCtx.createChannelMerger(1);
  merger.connect(worklet);
  window._civitasMerger      = merger;
  window._civitasConnectedEp = new Map(); // endpointId → AudioNode

  // Connecte un track distant (audio uniquement, jamais local)
  window._civitasConnectTrack = (track) => {
    if (track.isLocal() || track.getType() !== 'audio') return;
    const epId = track.getParticipantId();
    if (window._civitasConnectedEp.has(epId)) return;
    const stream = track.stream || track.getOriginalStream?.();
    const mt     = track.getTrack?.();
    const ms     = stream || (mt ? new MediaStream([mt]) : null);
    if (!ms) { console.warn('[CIVITAS] Pas de stream pour', epId); return; }
    try {
      const src = inCtx.createMediaStreamSource(ms);
      src.connect(merger);
      window._civitasConnectedEp.set(epId, src);
      console.log('[CIVITAS] Audio IN ✓ endpoint=' + epId);
    } catch(e) {
      console.warn('[CIVITAS] Audio IN err:', e.message);
    }
  };

  window._civitasDisconnectTrack = (epId) => {
    const src = window._civitasConnectedEp.get(epId);
    if (src) {
      try { src.disconnect(); } catch(e) {}
      window._civitasConnectedEp.delete(epId);
      console.log('[CIVITAS] Audio IN déconnecté endpoint=' + epId);
    }
  };

  // ── Sortant 24kHz ← Gemini ───────────────────────────────────────────────
  const outCtx  = new AudioContext({ sampleRate: 24000 });
  const outDest = outCtx.createMediaStreamDestination();
  window._civitasOutStream = outDest.stream;
  window._civitasOutCtx    = outCtx;

  let queue = [], playing = false;
  const playNext = () => {
    if (!queue.length) { playing = false; return; }
    playing = true;
    const samples = new Int16Array(queue.shift());
    const buf  = outCtx.createBuffer(1, samples.length, 24000);
    const data = buf.getChannelData(0);
    for (let i = 0; i < samples.length; i++) data[i] = samples[i] / 32768.0;
    const src = outCtx.createBufferSource();
    src.buffer = buf;
    src.connect(outDest);
    src.onended = playNext;
    src.start();
  };
  ws.onmessage = (e) => { queue.push(e.data); if (!playing) playNext(); };

  // ── Câblage via lib-jitsi-meet TRACK_ADDED + AUDIO_LEVEL ─────────────────
  const wireConf = (conf) => {
    const E  = JitsiMeetJS.events.conference;
    const TE = JitsiMeetJS.events.track;

    conf.on(E.TRACK_ADDED, (track) => {
      window._civitasConnectTrack(track);

      if (!track.isLocal() && track.getType() === 'audio') {
        const epId = track.getParticipantId();
        // TRACK_AUDIO_LEVEL_CHANGED — niveau par endpoint (RFC6464 côté client)
        track.addEventListener(TE.TRACK_AUDIO_LEVEL_CHANGED, (level) => {
          if (level > 0.015) {
            window.__civitasEvent?.('AUDIO_LEVEL', {
              participantId: epId,
              level: Math.round(level * 1000) / 1000,
            });
          }
        });
      }
    });

    conf.on(E.TRACK_REMOVED, (track) => {
      if (!track.isLocal() && track.getType() === 'audio')
        window._civitasDisconnectTrack(track.getParticipantId());
    });

    // Tracks déjà présents (room non-vide)
    conf.getParticipants?.().forEach(p =>
      p.getTracks?.().forEach(t => window._civitasConnectTrack(t))
    );
    console.log('[CIVITAS] Audio bridge via TRACK_ADDED ✓');
  };

  // Fallback DOM
  const fallbackDom = () => {
    console.warn('[CIVITAS] Fallback DOM audio');
    const conn = (el) => {
      if (!el.srcObject || el._civConn) return;
      el._civConn = true;
      try {
        const src = inCtx.createMediaStreamSource(el.srcObject);
        src.connect(merger);
        console.log('[CIVITAS] DOM audio connecté:', el.id);
      } catch(e) {}
    };
    document.querySelectorAll('audio').forEach(conn);
    new MutationObserver(() => document.querySelectorAll('audio').forEach(conn))
      .observe(document.body, { childList: true, subtree: true });
  };

  // Attente APP.conference._room
  let tries = 0;
  const timer = setInterval(() => {
    tries++;
    const conf = window.APP?.conference?._room;
    if (conf)       { clearInterval(timer); wireConf(conf); }
    else if (tries > 120) { clearInterval(timer); fallbackDom(); }
  }, 500);

  return 'audio_bridge_ready';
})
"""

# ─────────────────────────────────────────────────────────────────────────────
# JITSI EVENTS BRIDGE
#
# S'abonne à TOUS les événements Jitsi via lib-jitsi-meet.
# Remet tout vers Python via window.__civitasEvent (expose_function Playwright).
# Aucune logique métier ici — pure capture.
# ─────────────────────────────────────────────────────────────────────────────
JITSI_EVENTS_JS = """
(eventCallback) => {
  if (window._civitasEventsInstalled) return 'already_installed';
  window._civitasEventsInstalled = true;

  const getName = (id) => {
    try {
      const p = window.APP.conference._room.getParticipantById(id);
      return p ? (p.getDisplayName() || id) : id;
    } catch(e) { return id; }
  };

  const allParticipants = () => {
    try {
      return window.APP.conference._room.getParticipants().map(p => ({
        id:           p.getId(),
        name:         p.getDisplayName() || 'Inconnu',
        role:         p.getRole(),
        isMuted:      p.isAudioMuted(),
        isVideoMuted: p.isVideoMuted(),
        raisedHand:   p.hasRaisedHand ? p.hasRaisedHand() : false,
      }));
    } catch(e) { return []; }
  };

  let tries = 0;
  const timer = setInterval(() => {
    tries++;
    const conf = window.APP?.conference?._room;
    if (!conf && tries <= 120) return;
    clearInterval(timer);
    if (!conf) { console.warn('[CIVITAS Events] timeout'); return; }

    const E = JitsiMeetJS.events.conference;

    // Participants
    conf.on(E.USER_JOINED, (id, p) => eventCallback('USER_JOINED', {
      participantId: id, name: p.getDisplayName() || 'Inconnu',
      role: p.getRole(), participants: allParticipants(),
    }));

    conf.on(E.USER_LEFT, (id, p) => eventCallback('USER_LEFT', {
      participantId: id, name: p.getDisplayName() || 'Inconnu',
      participants: allParticipants(),
    }));

    conf.on(E.USER_ROLE_CHANGED, (id, role) => eventCallback('USER_ROLE_CHANGED', {
      participantId: id, name: getName(id), role,
    }));

    conf.on(E.DISPLAY_NAME_CHANGED, (id, name) => eventCallback('DISPLAY_NAME_CHANGED', {
      participantId: id, name,
    }));

    // Locuteur dominant — signal JVB certifié (DominantSpeakerEndpointChangeEvent)
    conf.on(E.DOMINANT_SPEAKER_CHANGED, (id, prev) => eventCallback('DOMINANT_SPEAKER_CHANGED', {
      participantId: id, name: getName(id), previousSpeakers: prev || [],
    }));

    // Audio
    conf.on(E.TALK_WHILE_MUTED, () => {
      const local = window.APP?.store?.getState()?.['features/base/participants']?.local;
      eventCallback('TALK_WHILE_MUTED', { participantId: local?.id, name: local?.name });
    });

    conf.on(E.NOISY_MIC, () => eventCallback('NOISY_MIC', {}));

    conf.on(E.TRACK_MUTE_CHANGED, (track) => {
      if (track.isLocal()) return;
      const pid = track.getParticipantId();
      eventCallback('TRACK_MUTE_CHANGED', {
        participantId: pid, name: getName(pid),
        type: track.getType(), muted: track.isMuted(),
      });
    });

    // Chat
    conf.on(E.MESSAGE_RECEIVED, (id, text, ts, nick) => eventCallback('MESSAGE_RECEIVED', {
      participantId: id, name: nick || getName(id),
      text, timestamp: ts, private: false,
    }));

    conf.on(E.PRIVATE_MESSAGE_RECEIVED, (id, text, ts, nick) => eventCallback('PRIVATE_MESSAGE_RECEIVED', {
      participantId: id, name: nick || getName(id),
      text, timestamp: ts, private: true,
    }));

    // Réactions
    conf.on(E.REACTION_RECEIVED, (id, reaction) => eventCallback('REACTION_RECEIVED', {
      participantId: id, name: getName(id), reaction,
    }));

    // Propriétés (levé de main, etc.)
    conf.on(E.PARTICIPANT_PROPERTY_CHANGED, (participant, prop, oldVal, newVal) => {
      const pid = participant.getId();
      eventCallback('PARTICIPANT_PROPERTY_CHANGED', {
        participantId: pid, name: getName(pid),
        property: prop, oldValue: oldVal, newValue: newVal,
        raisedHand: prop === 'raisedHand' ? (newVal === 'true' || newVal === true) : undefined,
      });
    });

    // Sondages
    conf.on(E.POLL_RECEIVED, (poll) => eventCallback('POLL_RECEIVED', {
      pollId: poll.id, question: poll.question, answers: poll.answers,
      senderId: poll.senderId, senderName: getName(poll.senderId),
    }));

    conf.on(E.POLL_ANSWER_RECEIVED, (answer) => eventCallback('POLL_ANSWER_RECEIVED', {
      pollId: answer.pollId, senderId: answer.senderId,
      senderName: getName(answer.senderId), answers: answer.answers,
    }));

    // Room
    conf.on(E.SUBJECT_CHANGED,    (s) => eventCallback('SUBJECT_CHANGED',    { subject: s }));
    conf.on(E.LOCK_STATE_CHANGED, (l) => eventCallback('LOCK_STATE_CHANGED', { locked: l }));

    conf.on(E.KICKED, (p, reason) => eventCallback('KICKED', {
      participantId: p?.getId?.(), name: p?.getDisplayName?.(), reason,
    }));

    conf.on(E.PARTICIPANT_KICKED, (kicker, kicked, reason) => eventCallback('PARTICIPANT_KICKED', {
      kickerId:   kicker?.getId?.(), kickerName: kicker?.getDisplayName?.(),
      kickedId:   kicked?.getId?.(), kickedName: kicked?.getDisplayName?.(), reason,
    }));

    // Snapshot initial
    const existing = allParticipants();
    if (existing.length > 0) eventCallback('PARTICIPANTS_SNAPSHOT', { participants: existing });

    console.log('[CIVITAS Events] ✓ ' + existing.length + ' participants présents');
  }, 500);

  return 'events_installing';
}
"""

ALONE_TIMEOUT_SECONDS = 600


class CivitasBrowser:
    """
    Chrome headless qui participe à une room Jitsi.
    Interface minimale — émet des événements, ne contient aucune logique métier.
    """

    def __init__(self, room_id: str, jitsi_host: str,
                 audio_pipe_port: int, ca_cert_path: str,
                 agent_name: str = "CIVITAS"):
        self.room_id         = room_id
        self.jitsi_host      = jitsi_host
        self.audio_pipe_port = audio_pipe_port
        self.ca_cert_path    = ca_cert_path
        self.agent_name      = agent_name

        self._playwright = None
        self._browser: Browser | None        = None
        self._context: BrowserContext | None = None
        self._page: Page | None              = None
        self._running    = False
        self._alone_task = None
        self._my_id: str | None = None

        # Callbacks — injectés par PeerInstance
        self.on_jitsi_event: callable | None  = None  # (event_type, data)
        self.on_chat_message: callable | None = None  # (sender, text, endpoint_id)
        self.on_alone: callable | None        = None

    async def start(self):
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox", "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--autoplay-policy=no-user-gesture-required",
                "--use-fake-ui-for-media-stream",
                "--use-fake-device-for-media-stream",
                "--disable-web-security",
                "--allow-running-insecure-content",
                "--ignore-certificate-errors",
            ],
        )
        self._context = await self._browser.new_context(
            ignore_https_errors=True,
            permissions=["microphone", "camera"],
            viewport={"width": 1280, "height": 720},
        )
        self._page = await self._context.new_page()
        self._running = True

        self._page.on("console", lambda m: log.debug(
            f"[Browser:{self.room_id}] JS[{m.type}]: {m.text}"
        ))
        self._page.on("pageerror", lambda e: log.warning(
            f"[Browser:{self.room_id}] JS ERROR: {e}"
        ))

        # Pont JS→Python — tous les événements Jitsi arrivent ici
        await self._page.expose_function("__civitasEvent", self._on_raw_event)

        from urllib.parse import quote
        url = (
            f"https://{self.jitsi_host}/{self.room_id}"
            f"#config.prejoinPageEnabled=false"
            f"&config.startWithAudioMuted=false"
            f"&config.startWithVideoMuted=true"
            f"&config.disableDeepLinking=true"
            f"&config.enableWelcomePage=false"
            f"&userInfo.displayName={quote(self.agent_name)}"
        )
        log.info(f"[Browser:{self.room_id}] → {url}")
        await self._page.goto(url, wait_until="domcontentloaded", timeout=30000)

        await self._bypass_prejoin()
        await self._wait_for_conference()
        await self._resolve_my_id()
        await self._inject_all()

        self._alone_task = asyncio.create_task(self._watch_alone())
        log.info(f"[Browser:{self.room_id}] Dans la room ✓ myId={self._my_id}")

    async def _resolve_my_id(self):
        try:
            result = await self._page.evaluate("""
                () => {
                    try { const id = window.APP?.conference?.myUserId?.(); if (id) return id; } catch(e) {}
                    try { return window.APP?.store?.getState()?.['features/base/participants']?.local?.id || null; } catch(e) {}
                    return null;
                }
            """)
            if result:
                self._my_id = result
                log.info(f"[Browser:{self.room_id}] myId={self._my_id}")
        except Exception as e:
            log.warning(f"[Browser:{self.room_id}] myId: {e}")

    async def _inject_all(self):
        # Ordre CRITIQUE : RTC spy d'abord (avant toute négociation SDP)
        await self._page.evaluate(RTC_SPY_JS)
        log.info(f"[Browser:{self.room_id}] RTC spy ✓")

        result = await self._page.evaluate(f"({AUDIO_BRIDGE_JS})({self.audio_pipe_port})")
        log.info(f"[Browser:{self.room_id}] Audio bridge: {result}")

        result = await self._page.evaluate(f"({JITSI_EVENTS_JS})(window.__civitasEvent)")
        log.info(f"[Browser:{self.room_id}] Events bridge: {result}")

    async def _on_raw_event(self, event_type: str, data: dict):
        """
        Reçoit TOUS les événements Jitsi depuis le JS.
        Dispatche chat vers on_chat_message, tout le reste vers on_jitsi_event.
        """
        # Chat — MESSAGE_RECEIVED natif Jitsi (plus fiable que Redux polling)
        if event_type in ("MESSAGE_RECEIVED", "PRIVATE_MESSAGE_RECEIVED"):
            pid    = data.get("participantId", "")
            sender = data.get("name", "Participant")
            text   = data.get("text", "").strip()
            # Filtrer nos propres messages
            if (self._my_id and pid == self._my_id) or self.agent_name.lower() in sender.lower():
                return
            if text and self.on_chat_message:
                asyncio.create_task(self.on_chat_message(sender, text, pid))
            return

        # Tout le reste → EventBus via on_jitsi_event
        if self.on_jitsi_event:
            asyncio.create_task(self.on_jitsi_event(event_type, data))

    async def _bypass_prejoin(self):
        await asyncio.sleep(2)
        for attempt in range(15):
            try:
                clicked = await self._page.evaluate("""
                    () => {
                        for (const sel of [
                            '[data-testid="prejoin-join-button"]', '.prejoin-preview .primary',
                            'button.primary', '[aria-label="Join meeting"]',
                            '[aria-label="Rejoindre la réunion"]',
                        ]) {
                            const btn = document.querySelector(sel);
                            if (btn) { btn.click(); return sel; }
                        }
                        if (document.querySelector('.toolbox-content-wrapper') ||
                            document.querySelector('#largeVideo')) return 'already';
                        return null;
                    }
                """)
                if clicked == 'already':
                    log.info(f"[Browser:{self.room_id}] Déjà en conférence")
                    return
                elif clicked:
                    log.info(f"[Browser:{self.room_id}] Préjoin cliqué ({clicked}) ✓")
                    await asyncio.sleep(2)
                    return
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] prejoin #{attempt+1}: {e}")
            await asyncio.sleep(1)
        log.warning(f"[Browser:{self.room_id}] Pas de préjoin — on continue")

    async def _wait_for_conference(self):
        await asyncio.sleep(2)
        for attempt in range(30):
            try:
                state = await self._page.evaluate("""
                    () => {
                        try { if (window.APP?.conference?.isJoined?.()) return { joined: true, method: 'isJoined' }; } catch(e) {}
                        try {
                            const c = window.APP?.store?.getState()?.['features/base/conference'];
                            if (c?.joined === true) return { joined: true, method: 'redux' };
                            return { joined: false };
                        } catch(e) { return { joined: false, error: e.message }; }
                    }
                """)
                if state and state.get('joined'):
                    log.info(f"[Browser:{self.room_id}] Conférence jointe ✓ ({state.get('method')})")
                    return
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] wait #{attempt+1}: {e}")
            await asyncio.sleep(1)
        log.warning(f"[Browser:{self.room_id}] Timeout conférence — on continue")

    async def _watch_alone(self):
        await asyncio.sleep(60)
        alone_since = None
        loop = asyncio.get_event_loop()
        while self._running:
            try:
                count = await self._page.evaluate("""
                    () => { try { const p = window.APP?.conference?.getParticipants?.(); return p !== undefined ? p.length : -1; } catch(e) { return -1; } }
                """)
                if count == 0:
                    if alone_since is None:
                        alone_since = loop.time()
                        log.info(f"[Browser:{self.room_id}] Seul — chrono {ALONE_TIMEOUT_SECONDS}s")
                    elif int(loop.time() - alone_since) >= ALONE_TIMEOUT_SECONDS:
                        log.info(f"[Browser:{self.room_id}] Seul 10min — arrêt")
                        if self.on_alone: asyncio.create_task(self.on_alone())
                        break
                elif count > 0 and alone_since is not None:
                    log.info(f"[Browser:{self.room_id}] {count} participant(s) — chrono annulé")
                    alone_since = None
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] watch_alone: {e}")
            await asyncio.sleep(10)

    async def send_chat(self, text: str):
        try:
            safe = text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
            await self._page.evaluate(f"""
                () => {{ window.APP?.store?.dispatch({{ type: 'SEND_MESSAGE', message: `{safe}`, ignorePrivacy: true }}); }}
            """)
            log.info(f"[Browser:{self.room_id}] Chat: {text[:80]}")
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] send_chat: {e}")

    # ─────────────────────────────────────────────────────────────────
    # Modération réelle — mêmes API que l'interface Jitsi elle-même
    # (JitsiConference.kickParticipant/muteParticipant, via l'objet
    # window.APP.conference._room, déjà utilisé ailleurs dans ce fichier
    # pour getParticipantById/getParticipants). Pas de simulation : ce
    # sont les mêmes appels que ceux déclenchés par les boutons "Kick"/
    # "Mute" de l'UI web Jitsi — même mécanisme XMPP réel côté Prosody.
    #
    # PRÉREQUIS IMPORTANT (comportement Jitsi standard, pas une limite de
    # cette implémentation) : ces actions n'ont d'effet QUE si le peer a
    # lui-même le rôle "moderator" dans la room au moment de l'appel. Par
    # défaut, Jitsi accorde ce rôle au PREMIER participant à rejoindre —
    # si un humain a créé la room avant que le peer ne la rejoigne (le cas
    # le plus courant : humain crée -> webhook -> peer rejoint ensuite),
    # le peer rejoint comme participant normal, PAS modérateur, et ces
    # appels échouent silencieusement côté Prosody (aucune erreur JS, la
    # commande est simplement ignorée côté serveur). Toujours vérifier
    # get_moderator_status() avant, et propager le résultat côté appelant
    # plutôt que de supposer un succès.
    # ─────────────────────────────────────────────────────────────────

    async def get_moderator_status(self) -> dict:
        """
        Rôle réel du peer dans la room, à l'instant T (peut changer en
        cours de réunion). JitsiParticipant.isModerator() compare le rôle
        MUC local à "moderator" — API lib-jitsi-meet réelle, pas déduite.
        """
        try:
            return await self._page.evaluate("""
                () => {
                    try {
                        const room = window.APP?.conference?._room;
                        if (!room) return { ok: false, error: 'room indisponible' };
                        const myId = room.myUserId ? room.myUserId() : null;
                        const me = myId ? room.getParticipantById(myId) : null;
                        const role = me?.getRole ? me.getRole() : null;
                        return { ok: true, participant_id: myId, role, is_moderator: role === 'moderator' };
                    } catch (e) {
                        return { ok: false, error: String(e && e.message || e) };
                    }
                }
            """)
        except Exception as e:
            return {"ok": False, "error": str(e)}

    async def kick_participant(self, participant_id: str, reason: str | None = None) -> dict:
        """
        Exclut un participant — JitsiConference.kickParticipant(id, reason).
        Cf. prérequis modérateur ci-dessus.
        """
        try:
            safe_reason = (reason or "").replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
            safe_id = participant_id.replace("\\", "\\\\").replace("'", "\\'")
            result = await self._page.evaluate(f"""
                () => {{
                    try {{
                        const room = window.APP?.conference?._room;
                        if (!room) return {{ ok: false, error: 'room indisponible' }};
                        room.kickParticipant('{safe_id}', `{safe_reason}`);
                        return {{ ok: true }};
                    }} catch (e) {{
                        return {{ ok: false, error: String(e && e.message || e) }};
                    }}
                }}
            """)
            if result.get("ok"):
                log.info(f"[Browser:{self.room_id}] Kick participant={participant_id} reason={reason!r}")
            else:
                log.warning(f"[Browser:{self.room_id}] Kick échoué participant={participant_id}: {result.get('error')}")
            return result
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] kick_participant: {e}")
            return {"ok": False, "error": str(e)}

    async def mute_participant(self, participant_id: str) -> dict:
        """
        Coupe le micro d'un participant à distance — JitsiConference.
        muteParticipant(id, 'audio'). Restriction VOLONTAIRE de Jitsi
        (confidentialité) : un modérateur peut couper un micro à distance
        mais ne peut JAMAIS le réactiver à la place du participant — seule
        la personne concernée peut se réactiver elle-même. Ce n'est pas une
        limite de cette implémentation, c'est le comportement Jitsi
        standard (aucune méthode "unmuteParticipant" n'existe côté API).
        Cf. prérequis modérateur ci-dessus.
        """
        try:
            safe_id = participant_id.replace("\\", "\\\\").replace("'", "\\'")
            result = await self._page.evaluate(f"""
                () => {{
                    try {{
                        const room = window.APP?.conference?._room;
                        if (!room) return {{ ok: false, error: 'room indisponible' }};
                        room.muteParticipant('{safe_id}', 'audio');
                        return {{ ok: true }};
                    }} catch (e) {{
                        return {{ ok: false, error: String(e && e.message || e) }};
                    }}
                }}
            """)
            if result.get("ok"):
                log.info(f"[Browser:{self.room_id}] Mute participant={participant_id}")
            else:
                log.warning(f"[Browser:{self.room_id}] Mute échoué participant={participant_id}: {result.get('error')}")
            return result
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] mute_participant: {e}")
            return {"ok": False, "error": str(e)}

    async def capture_frame(self) -> str | None:
        try:
            import base64
            png = await self._page.screenshot(type="jpeg", quality=80,
                clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            return base64.b64encode(png).decode()
        except Exception as e:
            log.warning(f"[Browser:{self.room_id}] capture_frame: {e}")
            return None

    async def stop(self):
        self._running = False
        if self._alone_task: self._alone_task.cancel()
        try:
            if self._page and not self._page.is_closed():
                await self._page.evaluate("() => { try { window.APP?.conference?.leave?.(); } catch(e) {} }")
                await asyncio.sleep(1)
        except Exception: pass
        for obj, m in [(self._context, 'close'), (self._browser, 'close'), (self._playwright, 'stop')]:
            try:
                if obj: await getattr(obj, m)()
            except Exception: pass
        log.info(f"[Browser:{self.room_id}] Fermé ✓")
