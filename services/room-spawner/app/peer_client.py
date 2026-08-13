import logging
import httpx
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {settings.PEER_SERVICE_TOKEN}",
    "Content-Type": "application/json",
}


async def join_room(room_id: str) -> dict:
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            f"{settings.PEER_SERVICE_URL}/peer/join",
            headers=HEADERS,
            json={"room_id": room_id},
        )
        if r.status_code == 200:
            log.info(f"[PeerClient] Peer rejoint room: {room_id}")
            return r.json()
        log.error(f"[PeerClient] Erreur join {room_id}: {r.status_code} {r.text}")
        return {}


async def leave_room(room_id: str) -> dict:
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.post(
            f"{settings.PEER_SERVICE_URL}/peer/leave/{room_id}",
            headers=HEADERS,
        )
        if r.status_code == 200:
            log.info(f"[PeerClient] Peer quitté room: {room_id}")
            return r.json()
        log.error(f"[PeerClient] Erreur leave {room_id}: {r.status_code} {r.text}")
        return {}


async def list_instances() -> dict:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(
            f"{settings.PEER_SERVICE_URL}/peer/instances",
            headers=HEADERS,
        )
        return r.json() if r.status_code == 200 else {}


async def kick_participant(room_id: str, participant_id: str, reason: str | None = None) -> dict:
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.post(
            f"{settings.PEER_SERVICE_URL}/peer/{room_id}/kick",
            headers=HEADERS,
            json={"participant_id": participant_id, "reason": reason},
        )
        if r.status_code == 200:
            return r.json()
        log.error(f"[PeerClient] Erreur kick {room_id}/{participant_id}: {r.status_code} {r.text}")
        return {"allowed": False, "ok": False, "error": f"peer-service {r.status_code}"}


async def mute_participant(room_id: str, participant_id: str) -> dict:
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.post(
            f"{settings.PEER_SERVICE_URL}/peer/{room_id}/mute",
            headers=HEADERS,
            json={"participant_id": participant_id},
        )
        if r.status_code == 200:
            return r.json()
        log.error(f"[PeerClient] Erreur mute {room_id}/{participant_id}: {r.status_code} {r.text}")
        return {"allowed": False, "ok": False, "error": f"peer-service {r.status_code}"}


async def moderator_status(room_id: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(
            f"{settings.PEER_SERVICE_URL}/peer/{room_id}/moderator_status",
            headers=HEADERS,
        )
        if r.status_code == 200:
            return r.json()
        return {"can_moderate": False, "is_moderator": None, "error": f"peer-service {r.status_code}"}
