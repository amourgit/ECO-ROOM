"""
CivitasBrowser — PORTÉ ET ÉTENDU DE services/peer/app/browser/browser.py.

Reste la porte n°2 unique vers Jitsi (doc 00 §2.2) : capteur (tous les événements
lib-jitsi-meet) et actionneur (toutes les actions du catalogue d'outils, doc 02).

Les 3 scripts injectés (RTC_SPY_JS, AUDIO_BRIDGE_JS, JITSI_EVENTS_JS) sont repris VERBATIM
(copier-coller contrôlé, cf. docs/architecture/04-plan-migration.md Phase 1 point 1) — ce sont
des scripts JS déjà validés en production, aucune raison de les modifier pour cette refonte.

Les méthodes d'action sont organisées en deux blocs :
  1. Actions déjà présentes dans l'ancien peer (✅ dans le catalogue, doc 02) — portées à
     l'identique.
  2. Nouvelles actions P0 (🆕 dans le catalogue, doc 02) — implémentées contre les méthodes
     réelles de `IJitsiConference` vérifiées dans le code source jitsi-meet
     (react/features/base/conference/reducer.ts), cf. doc 02 §0 "Méthode de vérification".

Les actions P1 (🔧 dans le catalogue) ne sont PAS implémentées ici : elles nécessitent une
vérification du format exact contre le bundle JS déployé avant tout code (doc 02 §11) — les
déclarer comme faussement fonctionnelles serait plus dangereux que de les omettre. Elles sont
seulement listées en commentaire en fin de fichier, comme rappel explicite du travail restant
(doc 04 Phase 5).
"""
import asyncio
import base64
import logging

from playwright.async_api import Browser, BrowserContext, Page, async_playwright

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# RTC SPY — intercepte setLocalDescription pour le replaceTrack audio sortant
# VERBATIM depuis services/peer/app/browser/browser.py — ne pas modifier sans
# revalider en conditions réelles (timing de négociation SDP).
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
  console.log('[CIVITAS] RTC spy \u2713');
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# AUDIO BRIDGE — VERBATIM depuis services/peer/app/browser/browser.py
# ─────────────────────────────────────────────────────────────────────────────
AUDIO_BRIDGE_JS = """
(async (wsPort) => {
  if (window._civitasAudioBridge) return 'already_running';
  window._civitasAudioBridge = true;

  const ws = new WebSocket(`ws://127.0.0.1:${wsPort}`);
  ws.binaryType = 'arraybuffer';
  window._civitasWS = ws;

  await new Promise((res, rej) => {
    ws.onopen  = res;
    ws.onerror = () => rej(new Error('WS failed'));
    setTimeout(() => rej(new Error('WS timeout')), 5000);
  });

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
  window._civitasConnectedEp = new Map();

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
      console.log('[CIVITAS] Audio IN \u2713 endpoint=' + epId);
    } catch(e) {
      console.warn('[CIVITAS] Audio IN err:', e.message);
    }
  };

  window._civitasDisconnectTrack = (epId) => {
    const src = window._civitasConnectedEp.get(epId);
    if (src) {
      try { src.disconnect(); } catch(e) {}
      window._civitasConnectedEp.delete(epId);
      console.log('[CIVITAS] Audio IN d\u00e9connect\u00e9 endpoint=' + epId);
    }
  };

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

  const wireConf = (conf) => {
    const E  = JitsiMeetJS.events.conference;
    const TE = JitsiMeetJS.events.track;

    conf.on(E.TRACK_ADDED, (track) => {
      window._civitasConnectTrack(track);

      if (!track.isLocal() && track.getType() === 'audio') {
        const epId = track.getParticipantId();
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

    conf.getParticipants?.().forEach(p =>
      p.getTracks?.().forEach(t => window._civitasConnectTrack(t))
    );
    console.log('[CIVITAS] Audio bridge via TRACK_ADDED \u2713');
  };

  const fallbackDom = () => {
    console.warn('[CIVITAS] Fallback DOM audio');
    const conn = (el) => {
      if (!el.srcObject || el._civConn) return;
      el._civConn = true;
      try {
        const src = inCtx.createMediaStreamSource(el.srcObject);
        src.connect(merger);
        console.log('[CIVITAS] DOM audio connect\u00e9:', el.id);
      } catch(e) {}
    };
    document.querySelectorAll('audio').forEach(conn);
    new MutationObserver(() => document.querySelectorAll('audio').forEach(conn))
      .observe(document.body, { childList: true, subtree: true });
  };

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
# JITSI EVENTS BRIDGE — VERBATIM depuis services/peer/app/browser/browser.py
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

    conf.on(E.DOMINANT_SPEAKER_CHANGED, (id, prev) => eventCallback('DOMINANT_SPEAKER_CHANGED', {
      participantId: id, name: getName(id), previousSpeakers: prev || [],
    }));

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

    conf.on(E.MESSAGE_RECEIVED, (id, text, ts, nick) => eventCallback('MESSAGE_RECEIVED', {
      participantId: id, name: nick || getName(id),
      text, timestamp: ts, private: false,
    }));

    conf.on(E.PRIVATE_MESSAGE_RECEIVED, (id, text, ts, nick) => eventCallback('PRIVATE_MESSAGE_RECEIVED', {
      participantId: id, name: nick || getName(id),
      text, timestamp: ts, private: true,
    }));

    conf.on(E.REACTION_RECEIVED, (id, reaction) => eventCallback('REACTION_RECEIVED', {
      participantId: id, name: getName(id), reaction,
    }));

    conf.on(E.PARTICIPANT_PROPERTY_CHANGED, (participant, prop, oldVal, newVal) => {
      const pid = participant.getId();
      eventCallback('PARTICIPANT_PROPERTY_CHANGED', {
        participantId: pid, name: getName(pid),
        property: prop, oldValue: oldVal, newValue: newVal,
        raisedHand: prop === 'raisedHand' ? (newVal === 'true' || newVal === true) : undefined,
      });
    });

    conf.on(E.POLL_RECEIVED, (poll) => eventCallback('POLL_RECEIVED', {
      pollId: poll.id, question: poll.question, answers: poll.answers,
      senderId: poll.senderId, senderName: getName(poll.senderId),
    }));

    conf.on(E.POLL_ANSWER_RECEIVED, (answer) => eventCallback('POLL_ANSWER_RECEIVED', {
      pollId: answer.pollId, senderId: answer.senderId,
      senderName: getName(answer.senderId), answers: answer.answers,
    }));

    conf.on(E.SUBJECT_CHANGED,    (s) => eventCallback('SUBJECT_CHANGED',    { subject: s }));
    conf.on(E.LOCK_STATE_CHANGED, (l) => eventCallback('LOCK_STATE_CHANGED', { locked: l }));

    conf.on(E.KICKED, (p, reason) => eventCallback('KICKED', {
      participantId: p?.getId?.(), name: p?.getDisplayName?.(), reason,
    }));

    conf.on(E.PARTICIPANT_KICKED, (kicker, kicked, reason) => eventCallback('PARTICIPANT_KICKED', {
      kickerId:   kicker?.getId?.(), kickerName: kicker?.getDisplayName?.(),
      kickedId:   kicked?.getId?.(), kickedName: kicked?.getDisplayName?.(), reason,
    }));

    const existing = allParticipants();
    if (existing.length > 0) eventCallback('PARTICIPANTS_SNAPSHOT', { participants: existing });

    console.log('[CIVITAS Events] \u2713 ' + existing.length + ' participants pr\u00e9sents');
  }, 500);

  return 'events_installing';
}
"""

ALONE_TIMEOUT_SECONDS = 600


class CivitasBrowser:
    """
    Chrome headless qui participe à UNE room Jitsi (garantie d'isolation, cf.
    docs/architecture/03-isolation-et-orchestration.md §2 : `room_id` fixé au constructeur,
    jamais réassigné). Émet des événements bruts (capteur) et expose les actions du catalogue
    d'outils (actionneur, doc 02) — aucune logique de décision ici, elle vit dans le graphe
    (app/graph/) et les outils qui l'appellent (app/tools/).
    """

    def __init__(self, room_id: str, jitsi_host: str,
                 audio_pipe_port: int, ca_cert_path: str,
                 agent_name: str = "CIVITAS"):
        self.room_id = room_id
        self.jitsi_host = jitsi_host
        self.audio_pipe_port = audio_pipe_port
        self.ca_cert_path = ca_cert_path
        self.agent_name = agent_name

        self._playwright = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None
        self._running = False
        self._alone_task = None
        self._my_id: str | None = None

        self.on_jitsi_event: callable | None = None    # (event_type, data)
        self.on_chat_message: callable | None = None    # (sender, text, endpoint_id)
        self.on_alone: callable | None = None

    @property
    def page(self) -> Page:
        """Exposé publiquement pour app/perception/vision.py (capture_frame)."""
        return self._page

    # ─────────────────────────────────────────────────────────────────
    # Cycle de vie — PORTÉ tel quel
    # ─────────────────────────────────────────────────────────────────

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

        self._page.on("console", lambda m: log.debug(f"[Browser:{self.room_id}] JS[{m.type}]: {m.text}"))
        self._page.on("pageerror", lambda e: log.warning(f"[Browser:{self.room_id}] JS ERROR: {e}"))

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
        log.info(f"[Browser:{self.room_id}] Dans la room \u2713 myId={self._my_id}")

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
        await self._page.evaluate(RTC_SPY_JS)
        log.info(f"[Browser:{self.room_id}] RTC spy \u2713")

        result = await self._page.evaluate(f"({AUDIO_BRIDGE_JS})({self.audio_pipe_port})")
        log.info(f"[Browser:{self.room_id}] Audio bridge: {result}")

        result = await self._page.evaluate(f"({JITSI_EVENTS_JS})(window.__civitasEvent)")
        log.info(f"[Browser:{self.room_id}] Events bridge: {result}")

    async def _on_raw_event(self, event_type: str, data: dict):
        if event_type in ("MESSAGE_RECEIVED", "PRIVATE_MESSAGE_RECEIVED"):
            pid = data.get("participantId", "")
            sender = data.get("name", "Participant")
            text = data.get("text", "").strip()
            if (self._my_id and pid == self._my_id) or self.agent_name.lower() in sender.lower():
                return
            if text and self.on_chat_message:
                asyncio.create_task(self.on_chat_message(sender, text, pid))
            return

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
                            '[aria-label="Rejoindre la r\u00e9union"]',
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
                    log.info(f"[Browser:{self.room_id}] D\u00e9j\u00e0 en conf\u00e9rence")
                    return
                elif clicked:
                    log.info(f"[Browser:{self.room_id}] Pr\u00e9join cliqu\u00e9 ({clicked}) \u2713")
                    await asyncio.sleep(2)
                    return
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] prejoin #{attempt+1}: {e}")
            await asyncio.sleep(1)
        log.warning(f"[Browser:{self.room_id}] Pas de pr\u00e9join — on continue")

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
                    log.info(f"[Browser:{self.room_id}] Conf\u00e9rence jointe \u2713 ({state.get('method')})")
                    return
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] wait #{attempt+1}: {e}")
            await asyncio.sleep(1)
        log.warning(f"[Browser:{self.room_id}] Timeout conf\u00e9rence — on continue")

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
                        log.info(f"[Browser:{self.room_id}] Seul 10min — arr\u00eat")
                        if self.on_alone: asyncio.create_task(self.on_alone())
                        break
                elif count > 0 and alone_since is not None:
                    log.info(f"[Browser:{self.room_id}] {count} participant(s) — chrono annul\u00e9")
                    alone_since = None
            except Exception as e:
                log.debug(f"[Browser:{self.room_id}] watch_alone: {e}")
            await asyncio.sleep(10)

    async def stop(self):
        self._running = False
        if self._alone_task:
            self._alone_task.cancel()
        try:
            if self._page and not self._page.is_closed():
                await self._page.evaluate("() => { try { window.APP?.conference?.leave?.(); } catch(e) {} }")
                await asyncio.sleep(1)
        except Exception:
            pass
        for obj, m in [(self._context, 'close'), (self._browser, 'close'), (self._playwright, 'stop')]:
            try:
                if obj:
                    await getattr(obj, m)()
            except Exception:
                pass
        log.info(f"[Browser:{self.room_id}] Ferm\u00e9 \u2713")

    # ═════════════════════════════════════════════════════════════════════════
    # BLOC 1 — Actions déjà présentes dans l'ancien peer (✅ doc 02), PORTÉES
    # ═════════════════════════════════════════════════════════════════════════

    async def send_chat(self, text: str):
        """✅ chat_tools.send_chat — doc 02 §1."""
        try:
            safe = text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
            await self._page.evaluate(f"""
                () => {{ window.APP?.store?.dispatch({{ type: 'SEND_MESSAGE', message: `{safe}`, ignorePrivacy: true }}); }}
            """)
            log.info(f"[Browser:{self.room_id}] Chat: {text[:80]}")
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] send_chat: {e}")

    async def get_moderator_status(self) -> dict:
        """✅ moderation_tools.get_moderator_status — doc 02 §3."""
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
        """✅ moderation_tools.kick_participant — doc 02 §3. Requiert le rôle moderator."""
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
                log.warning(f"[Browser:{self.room_id}] Kick \u00e9chou\u00e9 participant={participant_id}: {result.get('error')}")
            return result
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] kick_participant: {e}")
            return {"ok": False, "error": str(e)}

    async def mute_participant(self, participant_id: str) -> dict:
        """✅ moderation_tools.mute_participant — doc 02 §3. Ne peut jamais réactiver à distance."""
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
                log.warning(f"[Browser:{self.room_id}] Mute \u00e9chou\u00e9 participant={participant_id}: {result.get('error')}")
            return result
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] mute_participant: {e}")
            return {"ok": False, "error": str(e)}

    # ═════════════════════════════════════════════════════════════════════════
    # BLOC 2 — Nouvelles actions P0 (🆕 doc 02), groundées sur IJitsiConference
    # ═════════════════════════════════════════════════════════════════════════

    async def _call_room_method(self, method: str, *args) -> dict:
        """
        Fabrique interne commune à toutes les nouvelles actions P0 : appelle
        `window.APP.conference._room.<method>(...args)` et normalise le résultat en
        `{"ok": bool, "error": str|None}` — même contrat que kick_participant/mute_participant
        ci-dessus (doc 02 §9 "pattern de double-niveau d'échec généralisé").

        Les arguments sont sérialisés en JSON côté Python et parsés côté JS — plus sûr que la
        construction de chaînes gabarit utilisée pour kick/mute historiquement (conservée
        telle quelle ci-dessus pour ne pas modifier du code déjà validé), et suffisant pour des
        arguments structurés (dict, bool, liste) que le pattern historique ne gérait pas.
        """
        import json
        args_json = json.dumps(list(args))
        try:
            result = await self._page.evaluate(f"""
                (argsJson) => {{
                    try {{
                        const room = window.APP?.conference?._room;
                        if (!room) return {{ ok: false, error: 'room indisponible' }};
                        if (typeof room['{method}'] !== 'function') {{
                            return {{ ok: false, error: "méthode '{method}' absente de cette version de lib-jitsi-meet" }};
                        }}
                        const args = JSON.parse(argsJson);
                        room['{method}'](...args);
                        return {{ ok: true }};
                    }} catch (e) {{
                        return {{ ok: false, error: String(e && e.message || e) }};
                    }}
                }}
            """, args_json)
            if not result.get("ok"):
                log.warning(f"[Browser:{self.room_id}] {method}({args}) \u00e9chou\u00e9: {result.get('error')}")
            return result
        except Exception as e:
            log.error(f"[Browser:{self.room_id}] {method}: {e}")
            return {"ok": False, "error": str(e)}

    async def _read_room_property(self, method: str, *args):
        """Équivalent lecture de _call_room_method — retourne la valeur brute (ou None + log)."""
        import json
        args_json = json.dumps(list(args))
        try:
            return await self._page.evaluate(f"""
                (argsJson) => {{
                    try {{
                        const room = window.APP?.conference?._room;
                        if (!room || typeof room['{method}'] !== 'function') return null;
                        const args = JSON.parse(argsJson);
                        return room['{method}'](...args);
                    }} catch (e) {{ return null; }}
                }}
            """, args_json)
        except Exception as e:
            log.warning(f"[Browser:{self.room_id}] lecture {method}: {e}")
            return None

    # ── chat_tools (doc 02 §1) ──────────────────────────────────────────────
    async def send_private_chat(self, participant_id: str, text: str) -> dict:
        """🆕 chat_tools.send_private_chat — JitsiConference.sendPrivateTextMessage."""
        return await self._call_room_method("sendPrivateTextMessage", participant_id, text)

    async def send_reaction(self, reaction: str) -> dict:
        """🆕 chat_tools.send_reaction — JitsiConference.sendReaction."""
        return await self._call_room_method("sendReaction", reaction)

    # ── presence_tools (doc 02 §2) ──────────────────────────────────────────
    async def raise_hand(self) -> dict:
        """🆕 presence_tools.raise_hand — setLocalParticipantProperty('raisedHand', ts).
        Convention de valeur à valider contre la version déployée, cf. doc 02 §2."""
        import time
        return await self._call_room_method(
            "setLocalParticipantProperty", "raisedHand", int(time.time() * 1000)
        )

    async def lower_hand(self) -> dict:
        """🆕 presence_tools.lower_hand."""
        return await self._call_room_method("setLocalParticipantProperty", "raisedHand", False)

    async def set_display_name(self, name: str) -> dict:
        """🆕 presence_tools.set_display_name — JitsiConference.setDisplayName."""
        return await self._call_room_method("setDisplayName", name)

    # ── moderation_tools (doc 02 §3) ────────────────────────────────────────
    async def grant_moderator(self, participant_id: str) -> dict:
        """🆕 moderation_tools.grant_moderator — JitsiConference.grantOwner."""
        return await self._call_room_method("grantOwner", participant_id)

    async def enable_av_moderation(self, media_type: str = "audio") -> dict:
        """🆕 moderation_tools.enable_av_moderation — JitsiConference.enableAVModeration."""
        return await self._call_room_method("enableAVModeration", media_type)

    async def disable_av_moderation(self, media_type: str = "audio") -> dict:
        """🆕 moderation_tools.disable_av_moderation."""
        return await self._call_room_method("disableAVModeration", media_type)

    async def approve_unmute_request(self, participant_id: str, media_type: str = "audio") -> dict:
        """🆕 moderation_tools.approve_unmute_request — JitsiConference.avModerationApprove."""
        return await self._call_room_method("avModerationApprove", media_type, participant_id)

    async def reject_unmute_request(self, participant_id: str, media_type: str = "audio") -> dict:
        """🆕 moderation_tools.reject_unmute_request — JitsiConference.avModerationReject."""
        return await self._call_room_method("avModerationReject", media_type, participant_id)

    async def enable_lobby(self) -> dict:
        """🆕 moderation_tools.enable_lobby — JitsiConference.enableLobby."""
        return await self._call_room_method("enableLobby")

    async def disable_lobby(self) -> dict:
        """🆕 moderation_tools.disable_lobby."""
        return await self._call_room_method("disableLobby")

    async def lobby_approve_access(self, participant_id: str) -> dict:
        """🆕 moderation_tools.lobby_approve_access."""
        return await self._call_room_method("lobbyApproveAccess", participant_id)

    async def lobby_deny_access(self, participant_id: str) -> dict:
        """🆕 moderation_tools.lobby_deny_access."""
        return await self._call_room_method("lobbyDenyAccess", participant_id)

    # ── room_tools (doc 02 §4) ──────────────────────────────────────────────
    async def set_subject(self, subject: str) -> dict:
        """🆕 room_tools.set_subject — JitsiConference.setSubject."""
        return await self._call_room_method("setSubject", subject)

    async def lock_room(self, password: str) -> dict:
        """🆕 room_tools.lock_room — JitsiConference.lock."""
        return await self._call_room_method("lock", password)

    async def unlock_room(self) -> dict:
        """🆕 room_tools.unlock_room — JitsiConference.lock(null)."""
        return await self._call_room_method("lock", None)

    async def end_meeting(self) -> dict:
        """🆕 room_tools.end_meeting — JitsiConference.end(). Vérifier
        is_end_conference_supported() au préalable."""
        return await self._call_room_method("end")

    async def is_end_conference_supported(self) -> bool:
        """📖 room_tools.is_end_conference_supported."""
        return bool(await self._read_room_property("isEndConferenceSupported"))

    # ── media_tools (doc 02 §5) ─────────────────────────────────────────────
    async def start_recording(self, mode: str = "file", **options) -> dict:
        """🆕 media_tools.start_recording — JitsiConference.startRecording({mode, ...}).
        Nécessite Jibri configuré côté infra Jitsi (hors périmètre CIVITAS)."""
        payload = {"mode": mode, **options}
        return await self._call_room_method("startRecording", payload)

    async def stop_recording(self, mode: str = "file") -> dict:
        """🆕 media_tools.stop_recording — JitsiConference.stopRecording."""
        return await self._call_room_method("stopRecording", mode)

    async def get_transcription_status(self):
        """📖 media_tools.get_transcription_status."""
        return await self._read_room_property("getTranscriptionStatus")

    # ── capacités de lecture (doc 02 §10) ───────────────────────────────────
    async def get_participant_count(self) -> int:
        """📖 doc 02 §10 — JitsiConference.getParticipantCount."""
        return int(await self._read_room_property("getParticipantCount") or 0)

    async def get_breakout_rooms(self):
        """📖 room_tools.get_breakout_rooms — lecture seule, cf. doc 02 §4 pour la gestion
        (création/fermeture), classée P1."""
        return await self._read_room_property("getBreakoutRooms")

    async def get_polls(self):
        """📖 doc 02 §11 — lecture seule."""
        return await self._read_room_property("getPolls")

    # ═════════════════════════════════════════════════════════════════════════
    # BLOC 3 — Vision (doc 02 §7)
    # ═════════════════════════════════════════════════════════════════════════

    async def capture_frame(self) -> str | None:
        """✅ vision_tools.capture_frame — conservé ici pour compatibilité ; l'implémentation
        canonique vit désormais dans app/perception/vision.py (capture_frame(browser))."""
        try:
            png = await self._page.screenshot(
                type="jpeg", quality=80, clip={"x": 0, "y": 0, "width": 1280, "height": 720}
            )
            return base64.b64encode(png).decode()
        except Exception as e:
            log.warning(f"[Browser:{self.room_id}] capture_frame: {e}")
            return None


# ═════════════════════════════════════════════════════════════════════════════
# Outils P1 (🔧, doc 02) — VOLONTAIREMENT NON IMPLÉMENTÉS ICI.
#
# Rappel explicite (doc 04 Phase 5) — à traiter dans cet ordre :
#   - create_poll / answer_poll        : format sendMessage/sendCommand à extraire du bundle
#                                         JS déployé avant tout code (doc 02 §11).
#   - manage_breakout_rooms            : composant XMPP dédié, format à extraire (doc 02 §4).
#   - toggle_e2ee + setMediaEncryptionKey : revue de sécurité dédiée avant activation (doc 02 §4).
#   - start_recording(mode="stream")   : gestion sécurisée de la clé de stream (doc 02 §5).
#   - dial / create_sip_gateway_session : dépend d'une passerelle SIP configurée (doc 02 §4).
# Le registre d'outils (app/tools/registry.py) déclare ces outils avec un statut explicite
# "not_implemented" plutôt que de les omettre silencieusement — cf. doc 01 §9.
# ═════════════════════════════════════════════════════════════════════════════
