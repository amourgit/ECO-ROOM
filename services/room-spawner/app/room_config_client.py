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
    """
    Écrit directement dans la colonne dédiée `peer_enabled` (PATCH accepte ce
    champ au niveau racine — cf. RoomConfigUpdate). AVANT : écrivait dans
    extra_config.peer_enabled, jamais lu de là (is_peer_enabled lit
    permissions.peer_enabled) — donc sans effet réel — ET remplaçait tout
    extra_config au passage (perte de données silencieuse pour toute autre
    clé déjà présente). Corrigé — cf. §2.3/§7.5 PLAN_SYNCHRONISATION_ROOMS_JITSI.md.
    """
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.patch(
            f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}",
            headers=HEADERS,
            json={"peer_enabled": enabled},
        )
        return r.status_code == 200
