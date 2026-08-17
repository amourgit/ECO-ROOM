"""
main.py — point d'entrée du process CIVITAS Agent.

Assemble, pour LA SEULE room `settings.ROOM_ID` (garantie d'isolation, doc 03 §2) :
context/memory → perception/speech → browser → tools → graph, puis expose une API HTTP
strictement locale à cette room (doc 01 §8.1).

Boucle d'exécution : un unique `asyncio.Queue` reçoit à la fois les événements Control Plane
(forwardés par civitas-orchestrator, cf. app/kafka/control_ingress.py) et les événements Data
Plane (navigateur headless, moteur de parole, vision) — chaque événement déclenche une
invocation du graphe LangGraph (app/graph/build.py) contre le checkpoint de CETTE room.
"""
import asyncio
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone

import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException

from app.browser.driver import CivitasBrowser
from app.config import get_settings
from app.context.store import ContextStore
from app.events.bus import EventBus
from app.events.handlers import (
    make_kafka_handler,
    make_log_handler,
    make_moderation_handler,
    make_speaker_handler,
)
from app.graph.build import build_graph
from app.graph.checkpoint import build_checkpointer, thread_config
from app.graph.deps import GraphDeps
from app.kafka import producer as kafka
from app.kafka.control_ingress import control_event_queue, enqueue_control_event
from app.memory.client import get_room_history
from app.perception.audio_pipe import AudioPipe
from app.perception.speaker_tracker import SpeakerTracker
from app.room.config_client import get_agent_context
from app.speech.gemini_live import GeminiSession
from app.state import initial_state
from app.tools.registry import build_default_registry

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

settings = get_settings()

# Événements Data Plane (navigateur, moteur de parole, vision) rejoignent LA MÊME file que les
# événements Control Plane forwardés par l'orchestrateur (app/kafka/control_ingress.py) — un
# seul point d'entrée dans le graphe, cf. app/graph/build.py (entrée conditionnelle sur
# `domain`). Réutilisation assumée et documentée plutôt qu'une deuxième file redondante.
event_queue = control_event_queue


class AgentRuntime:
    """Regroupe tout l'état vivant du process — un seul par instance (doc 03 §2)."""

    def __init__(self):
        self.room_config: dict = {}
        self.context_store: ContextStore | None = None
        self.speaker_tracker: SpeakerTracker | None = None
        self.event_bus: EventBus | None = None
        self.audio_pipe: AudioPipe | None = None
        self.speech_engine: GeminiSession | None = None
        self.browser: CivitasBrowser | None = None
        self.tool_registry = None
        self.graph_deps: GraphDeps | None = None
        self.compiled_graph = None
        self.checkpointer_cm = None
        self.current_response_mode: str = "audio"
        self._process_task: asyncio.Task | None = None
        self._running = False


runtime = AgentRuntime()


def _push_event(domain: str, event_type: str, data: dict):
    """Empile un événement Data Plane dans la file unique (cf. commentaire en tête de module).
    Utilisé par tous les callbacks navigateur/moteur de parole/vision ci-dessous."""
    event_queue.put_nowait({"domain": domain, "event_type": event_type, "data": data})


async def _on_jitsi_event(event_type: str, data: dict):
    # Double émission volontaire : EventBus (réactions rapides/locales, doc 01 §8) ET
    # graphe LangGraph (raisonnement, doc 01 §6) — les deux mécanismes sont complémentaires,
    # pas redondants (cf. app/events/bus.py).
    if runtime.event_bus:
        await runtime.event_bus.emit(event_type, data)
    _push_event("data", event_type, data)


async def _on_chat_message(sender: str, text: str, participant_id: str):
    _push_event("data", "MESSAGE_RECEIVED", {"name": sender, "text": text, "participantId": participant_id})


async def _on_speech(text: str, turn_id: str | None):
    """Callback GeminiSession — réponse générée par l'agent (transcription de sortie)."""
    if not text:
        return
    runtime.context_store.add("", settings.ROOM_ID, text, entry_type="agent", turn_id=turn_id)
    _push_event("data", "AGENT_SPEECH", {"text": text, "turn_id": turn_id})
    # Livraison texte (chat) quand response_mode == "text" — l'audio a de toute façon déjà
    # commencé à être généré côté Gemini ; c'est `_on_audio` ci-dessous qui, selon le MÊME
    # `current_response_mode`, choisit de le transmettre ou non au navigateur. Cf. doc 02 §2.1
    # pour la justification de ce mécanisme (pas un track.mute() Jitsi).
    if runtime.current_response_mode == "text" and runtime.browser:
        await runtime.browser.send_chat(text)


async def _on_audio(pcm_24k: bytes):
    """Callback GeminiSession — PCM sortant. Transmis au navigateur uniquement en mode audio."""
    if runtime.current_response_mode == "audio" and runtime.audio_pipe:
        await runtime.audio_pipe.send_audio(pcm_24k)


async def _on_transcription(text: str, turn_id: str | None):
    """Callback GeminiSession — transcription ENTRANTE (ce qu'un participant a dit)."""
    if not text:
        return
    speaker_id = runtime.speaker_tracker.current_speaker()[0] if runtime.speaker_tracker else None
    speaker_name = runtime.speaker_tracker.current_speaker()[1] if runtime.speaker_tracker else "Participant"
    runtime.context_store.add(speaker_id or "", speaker_name, text, entry_type="participant", turn_id=turn_id)
    _push_event("data", "SPEECH_TRANSCRIPT", {"text": text, "turn_id": turn_id, "participantId": speaker_id})


async def _on_alone():
    log.info(f"[Runtime:{settings.ROOM_ID}] Seul depuis 10min — arrêt du process")
    await shutdown()


async def _process_loop():
    """Boucle principale : un événement en file = une invocation du graphe (doc 01 §6)."""
    cfg = thread_config(settings.ROOM_ID)
    while runtime._running:
        try:
            event = await event_queue.get()
        except asyncio.CancelledError:
            break
        try:
            result = await runtime.compiled_graph.ainvoke({"incoming_event": event}, config=cfg)
            if result and result.get("response_mode"):
                runtime.current_response_mode = result["response_mode"]
        except Exception as e:
            log.error(f"[Runtime:{settings.ROOM_ID}] Erreur graphe: {e}", exc_info=True)


async def startup():
    log.info(f"[Runtime:{settings.ROOM_ID}] Démarrage…")

    runtime.room_config = await get_agent_context(settings.ROOM_ID)
    history = await get_room_history(settings.ROOM_ID, limit=settings.HISTORY_REHYDRATE_LIMIT)

    runtime.context_store = ContextStore(settings.ROOM_ID)
    seeded = runtime.context_store.seed(history)
    log.info(f"[Runtime:{settings.ROOM_ID}] Mémoire réhydratée: {seeded} entrée(s)")

    runtime.speaker_tracker = SpeakerTracker(settings.ROOM_ID)
    runtime.event_bus = EventBus(settings.ROOM_ID)
    runtime.event_bus.register("*", make_speaker_handler(runtime.speaker_tracker))
    runtime.event_bus.register("*", make_log_handler(settings.ROOM_ID))
    runtime.event_bus.register("*", make_kafka_handler(settings.ROOM_ID, kafka))

    await kafka.start()

    runtime.audio_pipe = AudioPipe(settings.ROOM_ID, on_audio_in=lambda pcm: runtime.speech_engine.send_audio(pcm))
    audio_port = await runtime.audio_pipe.start()

    runtime.speech_engine = GeminiSession(
        room_id=settings.ROOM_ID,
        system_instruction=runtime.room_config.get("system_prompt", ""),
        on_speech=_on_speech,
        on_audio=_on_audio,
        on_transcription=_on_transcription,
        context_provider=lambda: runtime.context_store.build_context(settings.CONTEXT_MAX_ENTRIES),
    )
    await runtime.speech_engine.start()

    runtime.browser = CivitasBrowser(
        room_id=settings.ROOM_ID, jitsi_host=settings.JITSI_HOST,
        audio_pipe_port=audio_port, ca_cert_path=settings.JITSI_CA_CERT,
        agent_name=runtime.room_config.get("agent_name", "CIVITAS"),
    )
    runtime.browser.on_jitsi_event = _on_jitsi_event
    runtime.browser.on_chat_message = _on_chat_message
    runtime.browser.on_alone = _on_alone
    await runtime.browser.start()

    # EventBus.moderation dépend du browser + d'un peu de contexte (behavior_mode) — enregistré
    # après le démarrage du navigateur, à l'identique du séquencement de l'ancien peer.
    runtime.event_bus.register("*", make_moderation_handler(
        settings.ROOM_ID, runtime.browser, {"behavior_mode": runtime.room_config.get("behavior_mode")}
    ))

    runtime.tool_registry = build_default_registry(runtime.browser, runtime.speech_engine)

    runtime.graph_deps = GraphDeps(
        room_id=settings.ROOM_ID, room_config=runtime.room_config,
        browser=runtime.browser, speech_engine=runtime.speech_engine,
        tool_registry=runtime.tool_registry, context_store=runtime.context_store,
        kafka=kafka,
    )

    runtime.checkpointer_cm = build_checkpointer()
    checkpointer = await runtime.checkpointer_cm.__aenter__()
    runtime.compiled_graph = build_graph(runtime.graph_deps, checkpointer)

    # Seed de l'état initial si aucun checkpoint n'existe déjà pour cette room (redémarrage).
    cfg = thread_config(settings.ROOM_ID)
    existing = await runtime.compiled_graph.aget_state(cfg)
    if not existing or not existing.values:
        await runtime.compiled_graph.aupdate_state(cfg, initial_state(settings.ROOM_ID))
        log.info(f"[Runtime:{settings.ROOM_ID}] État initial créé")
    else:
        log.info(f"[Runtime:{settings.ROOM_ID}] Checkpoint existant repris")

    runtime._running = True
    runtime._process_task = asyncio.create_task(_process_loop())

    await kafka.publish_room_event(settings.ROOM_ID, "agent.started", {})
    log.info(f"[Runtime:{settings.ROOM_ID}] Prêt \u2713")


async def shutdown():
    log.info(f"[Runtime:{settings.ROOM_ID}] Arrêt…")
    runtime._running = False
    if runtime._process_task:
        runtime._process_task.cancel()
    await kafka.publish_room_event(settings.ROOM_ID, "agent.stopped", {})
    for obj in (runtime.browser, runtime.speech_engine, runtime.audio_pipe):
        if obj:
            try:
                await obj.stop()
            except Exception as e:
                log.warning(f"[Runtime:{settings.ROOM_ID}] stop(): {e}")
    if runtime.checkpointer_cm:
        try:
            await runtime.checkpointer_cm.__aexit__(None, None, None)
        except Exception:
            pass
    await kafka.stop()
    log.info(f"[Runtime:{settings.ROOM_ID}] Arrêté \u2713")


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await startup()
    yield
    await shutdown()


app = FastAPI(title=f"CIVITAS Agent — {settings.ROOM_ID}", lifespan=lifespan)


def _check_token(authorization: str = Header(default="")):
    if authorization != f"Bearer {settings.API_TOKEN}":
        raise HTTPException(status_code=401, detail="unauthorized")


@app.get("/health")
async def health():
    return {"status": "ok" if runtime._running else "starting", "room_id": settings.ROOM_ID}


@app.get("/admin/state")
async def get_state(_: None = Depends(_check_token)):
    cfg = thread_config(settings.ROOM_ID)
    snapshot = await runtime.compiled_graph.aget_state(cfg)
    return {"room_id": settings.ROOM_ID, "state": snapshot.values if snapshot else None,
            "tools": runtime.tool_registry.describe() if runtime.tool_registry else []}


@app.post("/control/event")
async def control_event(body: dict, _: None = Depends(_check_token)):
    """Ingress Control Plane — cf. docs/architecture/03-isolation-et-orchestration.md §4.6.
    Le room_id du body est vérifié mais n'a aucune autre utilité que la détection d'anomalie :
    ce process ne traite de toute façon jamais que settings.ROOM_ID (garantie structurelle,
    doc 03 §2)."""
    if body.get("room_id") and body["room_id"] != settings.ROOM_ID:
        raise HTTPException(status_code=400, detail="room_id mismatch — bug côté orchestrateur")
    await enqueue_control_event({"event_type": body.get("event_type"), "data": body.get("data", {})})
    return {"accepted": True}


@app.post("/admin/send_text")
async def admin_send_text(body: dict, _: None = Depends(_check_token)):
    await runtime.speech_engine.send_text(body["text"])
    return {"ok": True}


@app.post("/admin/send_chat")
async def admin_send_chat(body: dict, _: None = Depends(_check_token)):
    await runtime.browser.send_chat(body["text"])
    return {"ok": True}


@app.post("/admin/kick")
async def admin_kick(body: dict, _: None = Depends(_check_token)):
    return await runtime.browser.kick_participant(body["participant_id"], body.get("reason"))


@app.post("/admin/mute")
async def admin_mute(body: dict, _: None = Depends(_check_token)):
    return await runtime.browser.mute_participant(body["participant_id"])


@app.get("/admin/moderator_status")
async def admin_moderator_status(_: None = Depends(_check_token)):
    return await runtime.browser.get_moderator_status()


@app.post("/shutdown")
async def admin_shutdown(_: None = Depends(_check_token)):
    """Arrêt propre demandé par civitas-orchestrator (doc 03 §4.3 teardown)."""
    asyncio.create_task(shutdown())
    return {"ok": True, "shutting_down_at": datetime.now(timezone.utc).isoformat()}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
