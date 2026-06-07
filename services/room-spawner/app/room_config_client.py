import logging
import httpx
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {settings.ROOM_CONFIG_TOKEN}",
    "Content-Type": "application/json",
}


async def get_room_context(room_id: str) -> dict | None:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(
            f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}/context",
            headers=HEADERS,
        )
        if r.status_code == 200:
            return r.json()
        return None


async def is_peer_enabled(room_id: str) -> bool:
    """
    Vérifie si le peer doit être actif dans cette room.
    Retourne True si la config est active ou si aucune config n'existe (défaut).
    """
    context = await get_room_context(room_id)
    if context is None:
        return True
    return context.get("permissions", {}).get("peer_enabled", True)


async def set_peer_enabled(room_id: str, enabled: bool) -> bool:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.patch(
            f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}",
            headers=HEADERS,
            json={"extra_config": {"peer_enabled": enabled}},
        )
        return r.status_code == 200
