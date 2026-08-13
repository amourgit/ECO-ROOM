import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.peer.manager import peer_manager
from app.kafka import producer as kafka
from app.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
)
log = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("[CivitasPeer] Démarrage...")
    await kafka.start()
    log.info("[CivitasPeer] Kafka producer démarré ✓")
    yield
    log.info("[CivitasPeer] Arrêt...")
    await peer_manager.destroy_all()
    await kafka.stop()


app = FastAPI(
    title="CIVITAS Peer v3",
    description="Agent AI participant dans les rooms Jitsi",
    version="3.0.0",
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
    if token != settings.API_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalide")
    return token


class JoinRequest(BaseModel):
    room_id: str


class TextRequest(BaseModel):
    text: str


class ChatRequest(BaseModel):
    text: str


class KickRequest(BaseModel):
    participant_id: str
    reason: str | None = None


class MuteRequest(BaseModel):
    participant_id: str


@app.post("/peer/join")
async def join(body: JoinRequest, _: str = Depends(verify_token)):
    instance = await peer_manager.create(body.room_id)
    return {
        "status": "joined",
        "room_id": body.room_id,
        "active": instance.active,
        "agent_name": instance.context.get("agent_name", "CIVITAS"),
        "behavior_mode": instance.context.get("behavior_mode", "on_call"),
    }


@app.post("/peer/leave/{room_id}")
async def leave(room_id: str, _: str = Depends(verify_token)):
    await peer_manager.destroy(room_id)
    return {"status": "left", "room_id": room_id}


@app.post("/peer/{room_id}/send_text")
async def send_text(room_id: str, body: TextRequest, _: str = Depends(verify_token)):
    instance = peer_manager.get(room_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance introuvable")
    await instance.send_text(body.text)
    return {"status": "sent"}


@app.post("/peer/{room_id}/send_chat")
async def send_chat(room_id: str, body: ChatRequest, _: str = Depends(verify_token)):
    instance = peer_manager.get(room_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance introuvable")
    await instance.send_chat(body.text)
    return {"status": "sent"}


@app.post("/peer/{room_id}/kick")
async def kick_participant(room_id: str, body: KickRequest, _: str = Depends(verify_token)):
    """
    Exclut un participant de la room réelle — cf. PeerInstance.kick_participant
    pour les deux niveaux d'échec possibles (allowed=false : bloqué côté
    CIVITAS ; ok=false avec allowed=true : rejeté par Jitsi, le plus souvent
    faute de rôle "moderator" pour le peer dans cette room à cet instant).
    """
    instance = peer_manager.get(room_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance introuvable")
    result = await instance.kick_participant(body.participant_id, body.reason)
    await kafka.publish_agent_action(room_id, "kick_participant", {
        "participant_id": body.participant_id,
        "reason": body.reason,
        **result,
    })
    return result


@app.post("/peer/{room_id}/mute")
async def mute_participant(room_id: str, body: MuteRequest, _: str = Depends(verify_token)):
    """
    Coupe le micro d'un participant à distance — cf. PeerInstance.mute_participant.
    Rappel Jitsi standard : ne peut jamais réactiver un micro à la place du
    participant, seulement le couper (aucune méthode "unmute" distante
    n'existe côté API Jitsi).
    """
    instance = peer_manager.get(room_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance introuvable")
    result = await instance.mute_participant(body.participant_id)
    await kafka.publish_agent_action(room_id, "mute_participant", {
        "participant_id": body.participant_id,
        **result,
    })
    return result


@app.get("/peer/{room_id}/moderator_status")
async def moderator_status(room_id: str, _: str = Depends(verify_token)):
    """
    État réel (can_moderate CIVITAS + rôle Jitsi effectif) — à consulter
    avant d'attendre un succès de /kick ou /mute. Cf. PeerInstance.moderator_status.
    """
    instance = peer_manager.get(room_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance introuvable")
    return await instance.moderator_status()


@app.get("/peer/instances")
async def list_instances(_: str = Depends(verify_token)):
    return {
        "count": peer_manager.count(),
        "instances": peer_manager.list_active(),
    }


@app.get("/health")
async def health():
    return {
        "service": "civitas-peer",
        "version": "3.0.0",
        "status": "ok",
        "active_instances": peer_manager.count(),
        "jitsi_host": settings.JITSI_HOST,
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.SERVICE_HOST,
        port=settings.SERVICE_PORT,
        reload=False,
    )
