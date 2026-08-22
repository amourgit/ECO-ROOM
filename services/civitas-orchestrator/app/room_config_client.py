"""
room_config_client — ADAPTÉ DE services/room-spawner/app/room_config_client.py.

Vérifie `agent_enabled` (nouveau nom cible, cf. docs/architecture/04-plan-migration.md —
Migration Alembic A) avant tout spawn, avec repli sur `peer_enabled` pendant la période de
coexistence des deux orchestrateurs (doc 04 §Bascule progressive).

Note de correction : une première version de ce module lisait `agent_enabled`/`peer_enabled`
au niveau racine de la réponse `/rooms/{room_id}/context`. C'est incorrect — ces deux champs
sont imbriqués sous `permissions` dans `AgentContextResponse`
(services/room-config/app/schemas/room_config.py), exactement comme l'original
`is_peer_enabled()` de room-spawner le lisait déjà correctement
(`context.get("permissions", {}).get("peer_enabled", True)`). Corrigé ci-dessous pour lire le
même chemin imbriqué — sans cette correction, `is_agent_enabled()` retombait systématiquement
sur son défaut `True`, quoi qu'un modérateur ait fait via `/moderator/eject`, exactement le bug
historique déjà documenté pour `peer_enabled` avant sa propre correction (cf.
services/room-config/app/services/room_config_service.py::build_agent_context, commentaire
"Corrige le bug §2.3/§7.5 du plan").
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
                permissions = r.json().get("permissions", {})
                # agent_enabled prime, peer_enabled en repli (doc 04 §Migration Alembic A) —
                # chemin imbriqué sous permissions, cf. docstring de module.
                return bool(permissions.get("agent_enabled", permissions.get("peer_enabled", True)))
    except Exception as e:
        log.warning(f"[RoomConfig] Erreur vérification agent_enabled({room_id}): {e}")
    return True  # comportement par défaut inchangé depuis room-spawner : activé si indéterminé


async def set_agent_enabled(room_id: str, enabled: bool) -> bool:
    """
    Persiste l'activation/désactivation manuelle (`/moderator/inject`, `/moderator/eject`) —
    équivalent direct de `set_peer_enabled` (room-spawner), mais écrit `agent_enabled` (colonne
    racine de `RoomConfig`, PAS `permissions.agent_enabled` — cf. asymétrie déjà présente et
    documentée dans l'original : écriture au niveau racine via PATCH, lecture imbriquée via
    `/context`, cf. services/room-config/app/services/room_config_service.py). Le service
    room-config synchronise automatiquement `peer_enabled` en retour
    (`_sync_agent_peer_enabled`, doc 04 Migration Alembic A) — aucune double écriture requise
    ici.
    """
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.patch(
                f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}",
                headers=HEADERS,
                json={"agent_enabled": enabled},
            )
            if r.status_code == 200:
                return True
            log.error(f"[RoomConfig] Échec set_agent_enabled({room_id}, {enabled}): {r.status_code} {r.text}")
    except Exception as e:
        log.error(f"[RoomConfig] Erreur set_agent_enabled({room_id}, {enabled}): {e}")
    return False


async def set_behavior_mode(room_id: str, mode: str) -> bool:
    """
    Utilisé par `/moderator/standby` (mode="silent") et `/moderator/activate` (mode="on_call")
    — équivalent direct de la logique déjà inline dans l'ancien
    services/room-spawner/app/spawner.py::set_peer_standby (PATCH `behavior_mode` seul, sans
    toucher à `agent_enabled`/`peer_enabled` : standby ne coupe jamais l'agent, il le fait
    seulement taire — cf. docs/architecture/04-plan-migration.md).
    """
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            r = await c.patch(
                f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}",
                headers=HEADERS,
                json={"behavior_mode": mode},
            )
            if r.status_code == 200:
                return True
            log.error(f"[RoomConfig] Échec set_behavior_mode({room_id}, {mode}): {r.status_code} {r.text}")
    except Exception as e:
        log.error(f"[RoomConfig] Erreur set_behavior_mode({room_id}, {mode}): {e}")
    return False
