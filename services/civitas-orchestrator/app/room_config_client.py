"""
room_config_client — ADAPTÉ DE services/room-spawner/app/room_config_client.py. Vérifie
`agent_enabled` (nouveau nom cible, cf. docs/architecture/04-plan-migration.md — Migration
Alembic A) avant tout spawn, avec repli sur `peer_enabled` pendant la période de coexistence
des deux orchestrateurs (doc 04 §Bascule progressive).
"""
import logging

import httpx

from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {"Authorization": f"Bearer {settings.ROOM_CONFIG_TOKEN}", "Content-Type": "application/json"}


async def is_agent_enabled(room_id: str) -> bool:
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.get(f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}/context", headers=HEADERS)
            if r.status_code == 200:
                data = r.json()
                # cf. doc 04 §Migration Alembic A — agent_enabled prime, peer_enabled en repli
                return bool(data.get("agent_enabled", data.get("peer_enabled", True)))
    except Exception as e:
        log.warning(f"[RoomConfig] Erreur vérification agent_enabled({room_id}): {e}")
    return True  # comportement par défaut inchangé depuis room-spawner : activé si indéterminé
