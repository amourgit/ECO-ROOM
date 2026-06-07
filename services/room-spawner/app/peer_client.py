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
