import logging
import httpx
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {settings.ROOM_CONFIG_TOKEN}",
    "Content-Type": "application/json",
}


async def get_agent_context(room_id: str) -> dict:
    """
    Récupère la config complète de l'agent pour cette room.
    Crée une config par défaut si elle n'existe pas.
    """
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.get(
                f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}/context",
                headers=HEADERS,
            )
            if r.status_code == 200:
                log.info(f"[RoomConfig] Config chargée pour: {room_id}")
                return r.json()
    except Exception as e:
        log.warning(f"[RoomConfig] Erreur chargement config {room_id}: {e}")

    log.warning(f"[RoomConfig] Config par défaut pour: {room_id}")
    return _default_context(room_id)


def _default_context(room_id: str) -> dict:
    return {
        "room_id": room_id,
        "agent_name": "CIVITAS",
        "system_prompt": (
            "Tu es CIVITAS, un assistant IA dans une réunion en ligne. "
            "Tu réponds uniquement si on mentionne ton nom. "
            "Réponses concises et professionnelles en français."
        ),
        "behavior_mode": "on_call",
        "language": "fr",
        "permissions": {
            "can_speak": True,
            "can_write_chat": True,
            "can_use_tools": False,
            "can_use_rag": False,
            "can_moderate": False,
        },
        "invocation_keywords": ["civitas"],
        "tools_allowed": [],
    }


async def get_room_history(room_id: str, limit: int = 200) -> list[dict]:
    """
    Récupère l'historique complet et persistant de la réunion (Postgres, via
    room-config) — utilisé pour réhydrater la mémoire locale du peer au
    (re)join, y compris après un crash/redémarrage complet du process.

    Dégradation gracieuse : si l'appel échoue (room-config indisponible),
    on retourne une liste vide et le peer démarre avec un historique local
    vide, comme avant — jamais bloquant pour le join.
    """
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.get(
                f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}/history",
                params={"limit": limit},
                headers=HEADERS,
            )
            if r.status_code == 200:
                entries = r.json().get("entries", [])
                log.info(f"[RoomConfig] Historique chargé pour {room_id}: {len(entries)} entrée(s)")
                return entries
    except Exception as e:
        log.warning(f"[RoomConfig] Erreur chargement historique {room_id}: {e}")
    return []
