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
from app.room_config_client import is_agent_enabled, set_agent_enabled, set_behavior_mode

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
    """
    Injection manuelle — équivalent direct de l'ancien `inject_peer`
    (services/room-spawner/app/spawner.py) : persiste `agent_enabled=True` PUIS spawn si pas
    déjà actif (même ordre que l'original : la persistance a lieu même si le spawn échoue
    ensuite, pour qu'un rattrapage Kafka ultérieur retrouve la room activée).
    """
    await set_agent_enabled(room_id, True)
    if registry.is_active(room_id):
        return {"ok": True, "already_active": True, "status": "already_active"}
    handle = await runtime_provider.spawn(room_id, env={})
    registry.put(handle)
    registry.set_status(room_id, "healthy")
    return {"ok": True, "status": "injected", "container": handle["container_name"]}


@app.post("/moderator/eject/{room_id}")
async def moderator_eject(room_id: str, _: None = Depends(_check_token)):
    """
    Éjection manuelle — équivalent direct de l'ancien `eject_peer` : persiste
    `agent_enabled=False` PUIS détruit le container actif s'il y en a un (même ordre que
    l'original — cf. services/room-spawner/app/spawner.py::eject_peer).
    """
    await set_agent_enabled(room_id, False)
    handle = registry.get(room_id)
    if not handle:
        return {"ok": True, "status": "not_active"}
    await runtime_provider.teardown(handle)
    registry.remove(room_id)
    return {"ok": True, "status": "ejected"}


@app.post("/moderator/standby/{room_id}")
async def moderator_standby(room_id: str, _: None = Depends(_check_token)):
    """
    Met l'agent en mode figurant — présent dans la room mais silencieux, il écoute mais
    n'intervient jamais. Équivalent direct de l'ancien `set_peer_standby`
    (services/room-spawner/app/spawner.py) : persiste `behavior_mode=silent` SANS jamais
    toucher au container (ce n'est PAS une éjection — corrigé par rapport à une première
    version de ce module qui appelait, à tort, `agent_client.shutdown()` ici, cf.
    docs/architecture/04-plan-migration.md).

    Amélioration délibérée par rapport à l'original : si un agent est déjà actif pour cette
    room, on lui demande de recharger sa config immédiatement (`reload_config`) pour que le
    mode silencieux prenne effet EN DIRECT — l'ancien `set_peer_standby` ne faisait que le
    PATCH côté base, sans jamais notifier le peer déjà connecté (celui-ci ne relisait sa
    config qu'à son prochain démarrage, cf. services/peer/app/peer/instance.py::start,
    `self.context` chargé une seule fois). Documenté explicitement, pas silencieux.
    """
    ok = await set_behavior_mode(room_id, "silent")
    handle = registry.get(room_id)
    if handle:
        try:
            await agent_client.reload_config(handle)
        except Exception as e:
            log.warning(f"[Orchestrator] reload_config (standby) {room_id}: {e}")
    return {"ok": ok, "status": "standby", "live_reload": bool(handle)}


@app.post("/moderator/activate/{room_id}")
async def moderator_activate(room_id: str, _: None = Depends(_check_token)):
    """
    Sort l'agent du mode figurant — équivalent direct de l'ancien `activate_peer`
    (`behavior_mode=on_call`). NE spawn PAS un nouvel agent (corrigé par rapport à une
    première version de ce module qui aliasait, à tort, `activate` sur `inject` — l'original
    suppose un agent déjà actif, mis en veille via `/standby`, jamais éjecté). Même
    amélioration de rechargement en direct que `/standby` ci-dessus.
    """
    ok = await set_behavior_mode(room_id, "on_call")
    handle = registry.get(room_id)
    if handle:
        try:
            await agent_client.reload_config(handle)
        except Exception as e:
            log.warning(f"[Orchestrator] reload_config (activate) {room_id}: {e}")
    return {"ok": ok, "status": "active", "live_reload": bool(handle)}


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
