"""
Client HTTP vers room-config — ADAPTÉ DE services/peer/app/room/config_client.py.

Scindé en deux responsabilités par rapport à l'ancien fichier (cf.
docs/architecture/01-architecture-cible-civitas-agent.md §8, arborescence) :
  - CE module   : configuration de l'agent pour la room (get_agent_context) — "qui suis-je,
                  comment dois-je me comporter".
  - app/memory/client.py : historique de réunion (get_room_history) — mémoire niveau 2,
                  "qu'est-ce qui s'est déjà dit".

Le endpoint room-config lui-même (services/room-config) n'a besoin d'AUCUNE modification pour
cette scission — c'est une réorganisation côté client uniquement.
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


async def get_agent_context(room_id: str) -> dict:
    """
    Récupère la config complète de l'agent pour cette room. Crée une config par défaut côté
    room-config si elle n'existe pas encore (comportement serveur inchangé).

    NB : `room_id` est passé explicitement (plutôt que lu directement depuis
    `get_settings().ROOM_ID`) uniquement pour que cette fonction reste testable unitairement
    sans dépendre du singleton Settings — mais dans tout le reste du code applicatif, l'appelant
    ne passe jamais autre chose que `settings.ROOM_ID` (cf. app/main.py). Aucune route de ce
    client n'accepte de room_id venant d'une entrée utilisateur/réseau non fiable.
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
