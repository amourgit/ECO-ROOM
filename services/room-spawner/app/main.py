import asyncio
import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.config import get_settings
from app.kafka_consumer import start_consumer
from app import spawner, peer_client

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
)
log = logging.getLogger(__name__)
settings = get_settings()

_consumer_task = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _consumer_task
    log.info("[RoomSpawner] Démarrage...")
    _consumer_task = asyncio.create_task(start_consumer())
    log.info("[RoomSpawner] Consumer Kafka démarré ✓")
    yield
    if _consumer_task:
        _consumer_task.cancel()
        try:
            await _consumer_task
        except asyncio.CancelledError:
            pass
    log.info("[RoomSpawner] Arrêt")


app = FastAPI(
    title="CIVITAS Room Spawner",
    description="Gestion du cycle de vie des peers par room",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def verify_token(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    if token != settings.PEER_SERVICE_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalide")
    return token


class RoomAction(BaseModel):
    room_id: str


# ─────────────────────────────────────────────
# Endpoints modérateur — contrôle manuel du peer
# ─────────────────────────────────────────────

@app.post("/moderator/inject")
async def inject_peer(body: RoomAction, _: str = Depends(verify_token)):
    """
    Injecte le peer dans une room.
    Le peer rejoint immédiatement et devient actif.
    """
    return await spawner.inject_peer(body.room_id)


@app.post("/moderator/eject")
async def eject_peer(body: RoomAction, _: str = Depends(verify_token)):
    """
    Éjecte le peer d'une room.
    Le peer quitte immédiatement et la config mémorise ce choix.
    """
    return await spawner.eject_peer(body.room_id)


@app.post("/moderator/standby")
async def set_standby(body: RoomAction, _: str = Depends(verify_token)):
    """
    Met le peer en mode figurant (silent).
    Il reste dans la room mais n'intervient jamais.
    """
    return await spawner.set_peer_standby(body.room_id)


@app.post("/moderator/activate")
async def activate_peer(body: RoomAction, _: str = Depends(verify_token)):
    """
    Réactive le peer depuis le mode silent vers on_call.
    """
    from app.room_config_client import HEADERS
    import httpx
    async with httpx.AsyncClient(timeout=10) as c:
        await c.patch(
            f"{settings.ROOM_CONFIG_URL}/rooms/{body.room_id}",
            headers=HEADERS,
            json={"behavior_mode": "on_call"},
        )
    return {"status": "activated", "room_id": body.room_id}


# ─────────────────────────────────────────────
# Endpoints monitoring
# ─────────────────────────────────────────────

@app.get("/rooms/active")
async def active_rooms(_: str = Depends(verify_token)):
    """Liste des rooms où un peer est actif."""
    rooms = spawner.get_active_rooms()
    instances = await peer_client.list_instances()
    return {
        "active_rooms": rooms,
        "peer_instances": instances,
    }


@app.get("/health")
async def health():
    return {
        "service": "room-spawner",
        "status": "ok",
        "auto_join": settings.AUTO_JOIN,
        "auto_leave": settings.AUTO_LEAVE,
        "active_rooms": len(spawner.get_active_rooms()),
        "version": "1.0.0",
    }
