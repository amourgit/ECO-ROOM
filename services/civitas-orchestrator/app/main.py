"""
main.py — CIVITAS Agent Orchestrator. Cf. docs/architecture/03-isolation-et-orchestration.md §4.

Process unique, sans état de raisonnement — un registre `room_id → container` (app/registry.py),
un provider de spawn/teardown (app/docker_runtime.py), un forwarder d'événements
(app/forwarder.py), et les routes `/moderator/*` héritées de `room-spawner` pour compatibilité
CLI immédiate (doc 04).
"""
import asyncio
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException

from app import agent_client
from app.config import get_settings
from app.docker_runtime import DockerAgentRuntimeProvider
from app.forwarder import forward_event
from app.kafka_consumer import consume_forever
from app.registry import AgentRegistry
from app.room_config_client import is_agent_enabled

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

settings = get_settings()

registry = AgentRegistry()
runtime_provider = DockerAgentRuntimeProvider()
_consumer_task: asyncio.Task | None = None


async def _handle_kafka_event(event: dict):
    """
    Handler unique pour tout événement `jitsi.room.events`/`jitsi.participant.events` — cf.
    doc 03 §4.6 et §Phase 2 du plan de migration.
    """
    event_type = event.get("event_type", "")
    room_id = event.get("room_id")
    if not room_id:
        return

    if event_type in ("muc-room-created", "room.created"):
        if registry.is_active(room_id):
            log.info(f"[Orchestrator] Room déjà active, spawn ignoré: {room_id}")
            return
        if not await is_agent_enabled(room_id):
            log.info(f"[Orchestrator] agent_enabled=false pour {room_id} — pas de spawn")
            return
        handle = await runtime_provider.spawn(room_id, env={})
        registry.put(handle)
        registry.set_status(room_id, "healthy")
        log.info(f"[Orchestrator] Agent spawné pour room={room_id} → {handle['container_name']}")

    elif event_type in ("muc-room-destroyed", "room.destroyed"):
        handle = registry.get(room_id)
        if handle:
            await runtime_provider.teardown(handle)
            registry.remove(room_id)
            log.info(f"[Orchestrator] Agent détruit pour room={room_id}")

    else:
        await forward_event(registry, event)


async def startup():
    log.info("[Orchestrator] Démarrage…")
    # Reconstruction du registre depuis Docker — doc 03 §4.5. Un redémarrage de
    # l'Orchestrateur ne perd donc aucun agent déjà actif.
    for handle in await runtime_provider.list_running():
        registry.put(handle)
    log.info(f"[Orchestrator] Registre reconstruit: {len(registry.list_all())} agent(s)")

    global _consumer_task
    _consumer_task = asyncio.create_task(consume_forever(_handle_kafka_event))
    log.info("[Orchestrator] Prêt ✓")


async def shutdown():
    log.info("[Orchestrator] Arrêt…")
    if _consumer_task:
        _consumer_task.cancel()
    # NB : on ne détruit PAS les agents actifs ici — ils survivent au redémarrage de
    # l'Orchestrateur par conception (doc 03 §4.2, §4.5).


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await startup()
    yield
    await shutdown()


app = FastAPI(title="CIVITAS Agent Orchestrator", lifespan=lifespan)


def _check_token(authorization: str = Header(default="")):
    if authorization != f"Bearer {settings.MODERATOR_API_TOKEN}":
        raise HTTPException(status_code=401, detail="unauthorized")


def _require_handle(room_id: str):
    handle = registry.get(room_id)
    if not handle:
        raise HTTPException(status_code=404, detail=f"aucun agent actif pour room={room_id}")
    return handle


@app.get("/health")
async def health():
    return {"status": "ok", "active_agents": len(registry.list_all())}


@app.get("/moderator/instances")
async def list_instances(_: None = Depends(_check_token)):
    return {"agents": registry.list_all()}


@app.get("/moderator/status/{room_id}")
async def moderator_status(room_id: str, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.moderator_status(handle)


@app.post("/moderator/inject/{room_id}")
async def moderator_inject(room_id: str, _: None = Depends(_check_token)):
    if registry.is_active(room_id):
        return {"ok": True, "already_active": True}
    handle = await runtime_provider.spawn(room_id, env={})
    registry.put(handle)
    registry.set_status(room_id, "healthy")
    return {"ok": True, "container": handle["container_name"]}


@app.post("/moderator/eject/{room_id}")
async def moderator_eject(room_id: str, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    await runtime_provider.teardown(handle)
    registry.remove(room_id)
    return {"ok": True}


@app.post("/moderator/standby/{room_id}")
async def moderator_standby(room_id: str, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.shutdown(handle)  # arrêt propre — cf. teardown ordonné, doc 03 §4.3


@app.post("/moderator/activate/{room_id}")
async def moderator_activate(room_id: str, _: None = Depends(_check_token)):
    return await moderator_inject(room_id)


@app.post("/moderator/kick/{room_id}")
async def moderator_kick(room_id: str, body: dict, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.kick(handle, body["participant_id"], body.get("reason"))


@app.post("/moderator/mute/{room_id}")
async def moderator_mute(room_id: str, body: dict, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.mute(handle, body["participant_id"])


@app.post("/moderator/send-chat/{room_id}")
async def moderator_send_chat(room_id: str, body: dict, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.send_chat(handle, body["text"])


@app.post("/moderator/send-text/{room_id}")
async def moderator_send_text(room_id: str, body: dict, _: None = Depends(_check_token)):
    handle = _require_handle(room_id)
    return await agent_client.send_text(handle, body["text"])


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
