"""
Client de mémoire niveau 2 ("tiède", Postgres via room-config) — cf.
docs/architecture/01-architecture-cible-civitas-agent.md §7.

ADAPTÉ DE la fonction get_room_history de services/peer/app/room/config_client.py (scission
documentée dans app/room/config_client.py). room-config reste la source de vérité durable —
inchangée, schéma `room_history_entries` inchangé (cf. docs/architecture/00-etat-des-lieux.md
§6.2).
"""
import logging

import httpx

from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {settings.ROOM_CONFIG_TOKEN}",
    "Content-Type": "application/json",
}


async def get_room_history(room_id: str, limit: int = 200) -> list[dict]:
    """
    Récupère l'historique complet et persistant de la réunion — utilisé pour réhydrater
    ContextStore (mémoire niveau 1) au démarrage du process, y compris après un crash/
    redémarrage complet (cf. doc 03 — le process qui redémarre est toujours celui de LA MÊME
    room, jamais un autre : `room_id` ici est systématiquement `settings.ROOM_ID`).

    Dégradation gracieuse : si l'appel échoue (room-config indisponible), on retourne une
    liste vide et le process démarre avec un historique local vide plutôt que de bloquer le
    démarrage de l'agent — comportement identique à l'ancien peer.
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
                log.info(f"[Memory] Historique chargé pour {room_id}: {len(entries)} entrée(s)")
                return entries
    except Exception as e:
        log.warning(f"[Memory] Erreur chargement historique {room_id}: {e}")
    return []
