"""
PeerInstance — orchestrateur d'un agent CIVITAS dans une room Jitsi.

Architecture modulaire LangGraph-ready :
  - EventBus : dispatche tous les événements Jitsi vers des handlers indépendants
  - SpeakerTracker : identification locuteur (dominant speaker JVB + audio levels)
  - Handlers : speaker, log, kafka, moderation — composables et extensibles
  - PeerInstance : orchestre audio + chat + vision

Règle audio fondamentale (cf. app/peer/response_policy.py) :
  Une sollicitation vocale obtient toujours une réponse vocale.
  Une sollicitation écrite (chat) obtient une réponse écrite par défaut,
  sauf demande explicite d'une réponse orale.

Transcription : chaque tour Gemini (entrée participant + réponse agent) est
accumulé et restitué en UNE fois, texte complet, jamais en fragments —
cf. GeminiSession._accumulate/_flush.
"""
import asyncio
import logging
import time
from datetime import datetime

from app.config import get_settings
from app.audio.pipe import AudioPipe
from app.gemini.session import GeminiSession
from app.browser.browser import CivitasBrowser
from app.context.store import ContextStore
from app.room.config_client import get_agent_context, get_room_history
from app.kafka import producer as kafka
from app.events.bus import EventBus
from app.events.handlers import (
    make_speaker_handler,
    make_log_handler,
    make_kafka_handler,
    make_moderation_handler,
)
from app.speaker.tracker import SpeakerTracker
from app.peer.response_policy import ResponseMode, decide_chat_response_mode, parse_keywords

settings = get_settings()
log = logging.getLogger(__name__)
ORAL_KEYWORDS = parse_keywords(settings.ORAL_REQUEST_KEYWORDS)


class PeerInstance:
    def __init__(self, room_id: str):
        self.room_id    = room_id
        self.active     = False
        self.started_at = datetime.utcnow()
        self.store      = ContextStore(room_id)
        self.context: dict = {}

        self.pipe:    AudioPipe      | None = None
        self.gemini:  GeminiSession  | None = None
        self.browser: CivitasBrowser | None = None

        self._response_mode: ResponseMode = ResponseMode.AUDIO

        self.tracker = SpeakerTracker(room_id)
        self.bus     = EventBus(room_id)

    # ─────────────────────────────────────────────────────────────────────────
    # Watcher connexion Jitsi
    # ─────────────────────────────────────────────────────────────────────────

    async def _watch_connection(self):
        """Surveille la connexion Jitsi — si perdue, stoppe et nettoie."""
        await asyncio.sleep(30)
        while self.active:
            try:
                if self.browser and self.browser._page and not self.browser._page.is_closed():
                    joined = await self.browser._page.evaluate("""
                        () => {
                            try {
                                return window.APP?.conference?.isJoined?.() ?? false;
                            } catch(e) { return false; }
                        }
                    """)
                    if not joined:
                        log.warning(f"[Peer:{self.room_id}] Connexion Jitsi perdue — nettoyage")
                        await self.stop()
                        from app.peer.manager import peer_manager
                        peer_manager.remove(self.room_id)
                        return
            except Exception as e:
                log.warning(f"[Peer:{self.room_id}] Watch error: {e}")
            await asyncio.sleep(10)

    # ─────────────────────────────────────────────────────────────────────────
    # Lifecycle
    # ─────────────────────────────────────────────────────────────────────────

    async def start(self):
        log.info(f"[Peer:{self.room_id}] Démarrage...")

        self.context  = await get_agent_context(self.room_id)
        agent_name    = self.context.get("agent_name", "CIVITAS")
        system_prompt = self.context.get("system_prompt", "")

        log.info(f"[Peer:{self.room_id}] Agent={agent_name} Mode={self.context.get('behavior_mode')}")

        # Réhydratation de la mémoire de réunion — couvre aussi bien le
        # premier join (réunion déjà en cours si ce peer redémarre après un
        # crash) que tout redémarrage complet du process. Dégradation
        # gracieuse : historique vide si room-config est injoignable.
        history = await get_room_history(self.room_id, limit=settings.HISTORY_REHYDRATE_LIMIT)
        seeded  = self.store.seed(history)
        if seeded:
            log.info(f"[Peer:{self.room_id}] Mémoire réhydratée : {seeded} entrée(s)")

        self.bus.register("*", make_speaker_handler(self.tracker))
        self.bus.register("*", make_log_handler(self.room_id))
        self.bus.register("*", make_kafka_handler(self.room_id, kafka))

        self.pipe = AudioPipe(room_id=self.room_id, on_audio_in=self._on_audio_in)
        pipe_port = await self.pipe.start()

        self.gemini = GeminiSession(
            room_id=self.room_id,
            system_instruction=system_prompt,
            on_speech=self._on_agent_speech,
            on_audio=self._on_gemini_audio,
            on_transcription=self._on_participant_speech,
            context_provider=self._build_catchup_context,
        )
        await self.gemini.start()

        self.browser = CivitasBrowser(
            room_id=self.room_id,
            jitsi_host=settings.JITSI_HOST,
            audio_pipe_port=pipe_port,
            ca_cert_path=settings.JITSI_CA_CERT,
            agent_name=agent_name,
        )
        self.browser.on_jitsi_event  = self._on_jitsi_event
        self.browser.on_chat_message = self._on_chat_message
        self.browser.on_alone        = self._on_alone
        await self.browser.start()

        self.bus.register("*", make_moderation_handler(
            self.room_id, self.browser, self.context
        ))

        try:
            await self.pipe.wait_connected(timeout=20.0)
            log.info(f"[Peer:{self.room_id}] AudioPipe ✓")
        except asyncio.TimeoutError:
            log.warning(f"[Peer:{self.room_id}] AudioPipe timeout")

        self.active = True
        log.info(f"[Peer:{self.room_id}] Actif ✓")

        # Lancer le watcher de connexion Jitsi
        asyncio.create_task(self._watch_connection())

        await kafka.publish_room_event(self.room_id, "peer.joined", {
            "agent_name": agent_name,
            "behavior_mode": self.context.get("behavior_mode"),
        })

        if self.context.get("behavior_mode") != "silent":
            await asyncio.sleep(2)
            keywords = self.context.get("invocation_keywords", ["civitas"])
            await self.browser.send_chat(
                f"👋 Bonjour ! Je suis {agent_name}. "
                f"Mentionnez mon nom ({', '.join(keywords)}) pour m'interpeller."
            )

    async def stop(self):
        if not self.active:
            return
        self.active = False
        agent_name = self.context.get("agent_name", "CIVITAS")
        try:
            if self.context.get("behavior_mode") != "silent":
                await self.browser.send_chat(f"{agent_name} se déconnecte. À bientôt !")
        except Exception: pass
        if self.browser: await self.browser.stop()
        if self.gemini:  await self.gemini.stop()
        if self.pipe:    await self.pipe.stop()
        await kafka.publish_room_event(self.room_id, "peer.left", {"agent_name": agent_name})
        log.info(f"[Peer:{self.room_id}] Arrêté ✓")

    def _build_catchup_context(self) -> str:
        """
        Fournit le texte de mémoire à injecter à chaque (re)connexion Gemini.
        Lecture purement locale (RAM) — jamais bloquant, jamais dépendant du
        réseau, donc fiable même si c'est une panne réseau qui vient de
        provoquer la reconnexion.
        """
        if self.store.is_empty:
            return ""
        return self.store.build_context(max_entries=settings.CONTEXT_MAX_ENTRIES)

    # ─────────────────────────────────────────────────────────────────────────
    # Événements Jitsi → EventBus
    # ─────────────────────────────────────────────────────────────────────────

    async def _on_jitsi_event(self, event_type: str, data: dict):
        await self.bus.emit(event_type, data)
        if event_type == "DOMINANT_SPEAKER_CHANGED":
            snapshot = self.tracker.snapshot()
            await kafka.publish_room_event(self.room_id, "room.dominant_speaker", {
                "dominant_speaker": snapshot["dominant_speaker"],
                "current_speaker":  snapshot["current_speaker"],
                "participants":     snapshot["room_participants"],
            })

    # ─────────────────────────────────────────────────────────────────────────
    # Audio
    # ─────────────────────────────────────────────────────────────────────────

    async def _on_audio_in(self, pcm: bytes):
        if self.gemini and self.context.get("behavior_mode") != "silent":
            await self.gemini.send_audio(pcm)

    async def _on_gemini_audio(self, pcm: bytes):
        if self.pipe and self._response_mode != ResponseMode.TEXT:
            await self.pipe.send_audio(pcm)

    # ─────────────────────────────────────────────────────────────────────────
    # Transcription
    # ─────────────────────────────────────────────────────────────────────────

    async def _on_agent_speech(self, text: str, turn_id: str | None = None):
        if not text.strip():
            return
        agent_name = self.context.get("agent_name", "CIVITAS")
        self.store.add("civitas-peer", agent_name, text, "agent", turn_id=turn_id)
        await kafka.publish_transcription(
            self.room_id, agent_name, text, "agent",
            speaker_id="civitas-peer",
            extra={"turn_id": turn_id} if turn_id else None,
        )
        if self._response_mode == ResponseMode.TEXT:
            # Le texte est déjà complet (accumulé par tour côté GeminiSession) :
            # plus besoin de bufferiser/débouncer comme avant, on poste
            # directement — c'était un contournement du fragmentement, résolu
            # à la source désormais.
            if self.browser:
                await self.browser.send_chat(f"{agent_name}: {text.strip()}")
            self._response_mode = ResponseMode.AUDIO  # retour au mode par défaut

    async def _on_participant_speech(self, text: str, turn_id: str | None = None):
        if not text.strip():
            return
        ep_id, name = self.tracker.current_speaker()
        log.info(f"[Peer:{self.room_id}] 🗣 [{name} / {ep_id}]: {text[:100]}")
        self.store.add(ep_id or "participant", name, text, "participant", turn_id=turn_id)
        # Une seule publication (ex-doublon corrigé : publish_transcription()
        # ET ce publish() explicite écrivaient tous les deux sur
        # room.transcriptions pour le même événement).
        await kafka.publish_transcription(
            self.room_id, name, text, "participant",
            speaker_id=ep_id,
            extra={"room_snapshot": self.tracker.snapshot(), "turn_id": turn_id},
        )
        text_lower = text.lower()
        keywords   = self.context.get("invocation_keywords", ["civitas"])
        vision_kw  = ["regarde", "vois", "écran", "capture", "screenshot", "analyse"]
        if any(k in text_lower for k in keywords) and any(v in text_lower for v in vision_kw):
            asyncio.create_task(self._handle_vision(text))

    # ─────────────────────────────────────────────────────────────────────────
    # Chat
    # ─────────────────────────────────────────────────────────────────────────

    async def _on_chat_message(self, sender: str, text: str, endpoint_id: str):
        self.store.add(endpoint_id, sender, f"[chat] {text}", "chat")
        await kafka.publish_transcription(
            self.room_id, sender, text, "chat", speaker_id=endpoint_id
        )
        if self.context.get("behavior_mode") == "silent":
            return
        text_lower = text.lower()
        keywords   = self.context.get("invocation_keywords", ["civitas"])
        if not any(k in text_lower for k in keywords):
            return
        vision_kw = ["regarde", "vois-tu", "écran", "screenshot"]
        if any(k in text_lower for k in vision_kw):
            asyncio.create_task(self._handle_vision(text, chat_mode=True))
            return

        self._response_mode = decide_chat_response_mode(text, ORAL_KEYWORDS)
        snap = self.tracker.snapshot()

        if self._response_mode == ResponseMode.AUDIO:
            await self.gemini.send_text(
                f"Contexte room: {snap['total_participants']} participants.\n"
                f"{sender} te demande de répondre vocalement: {text}\n"
                f"Réponds en audio."
            )
        else:
            names = [p["display_name"] for p in snap["room_participants"].values()]
            await self.gemini.send_text(
                f"Contexte room: {snap['total_participants']} participant(s): {', '.join(names)}.\n"
                f"{sender} t'écrit dans le chat: {text}\n"
                f"Réponds par écrit (1-2 phrases max en {self.context.get('language', 'fr')})."
            )

    # ─────────────────────────────────────────────────────────────────────────
    # Vision
    # ─────────────────────────────────────────────────────────────────────────

    async def _handle_vision(self, original_text: str, chat_mode: bool = False):
        if not self.browser:
            return
        agent_name = self.context.get("agent_name", "CIVITAS")
        await self.browser.send_chat(f"{agent_name}: 📸 Capture en cours...")
        frame = await self.browser.capture_frame()
        if not frame:
            await self.browser.send_chat(f"{agent_name}: Impossible de capturer.")
            return
        self._response_mode = ResponseMode.TEXT
        await self.gemini.send_image(frame, "Décris ce que tu vois dans cette réunion Jitsi en français.")
        await kafka.publish_agent_action(self.room_id, "vision_capture", {"triggered_by": original_text})

    # ─────────────────────────────────────────────────────────────────────────
    # Alone
    # ─────────────────────────────────────────────────────────────────────────

    async def _on_alone(self):
        log.info(f"[Peer:{self.room_id}] Seul — arrêt")
        await self.stop()
        from app.peer.manager import peer_manager
        peer_manager.remove(self.room_id)

    # ─────────────────────────────────────────────────────────────────────────
    # API publique
    # ─────────────────────────────────────────────────────────────────────────

    async def send_text(self, text: str):
        if self.gemini: await self.gemini.send_text(text)

    async def send_chat(self, text: str):
        if self.browser: await self.browser.send_chat(text)

    @property
    def room_snapshot(self) -> dict:
        return self.tracker.snapshot()




