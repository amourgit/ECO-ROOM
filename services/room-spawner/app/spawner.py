import asyncio
import logging
from app import peer_client, room_config_client
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

# État local des rooms actives
_active_rooms: set[str] = set()
_lock = asyncio.Lock()


async def on_room_created(room_id: str):
    """
    Appelé quand Prosody notifie qu'une room a été créée.
    Rejoint automatiquement si AUTO_JOIN et peer activé dans config.
    """
    if not settings.AUTO_JOIN:
        log.info(f"[Spawner] AUTO_JOIN désactivé — room ignorée: {room_id}")
        return

    enabled = await room_config_client.is_peer_enabled(room_id)
    if not enabled:
        log.info(f"[Spawner] Peer désactivé pour room: {room_id} — skip")
        return

    async with _lock:
        if room_id in _active_rooms:
            log.warning(f"[Spawner] Peer déjà actif dans: {room_id}")
            return
        _active_rooms.add(room_id)

    log.info(f"[Spawner] Room créée → instanciation peer: {room_id}")
    result = await peer_client.join_room(room_id)
    if not result:
        async with _lock:
            _active_rooms.discard(room_id)
        log.error(f"[Spawner] Échec instanciation peer: {room_id}")


async def on_room_destroyed(room_id: str):
    """
    Appelé quand Prosody notifie qu'une room a été détruite.
    Éjecte le peer automatiquement si AUTO_LEAVE.
    """
    if not settings.AUTO_LEAVE:
        return

    async with _lock:
        if room_id not in _active_rooms:
            return
        _active_rooms.discard(room_id)

    log.info(f"[Spawner] Room détruite → éjection peer: {room_id}")
    await peer_client.leave_room(room_id)


async def inject_peer(room_id: str) -> dict:
    """
    Injection manuelle du peer dans une room par un modérateur.
    Met à jour la config pour activer le peer.
    """
    async with _lock:
        if room_id in _active_rooms:
            return {"status": "already_active", "room_id": room_id}
        _active_rooms.add(room_id)

    await room_config_client.set_peer_enabled(room_id, True)
    log.info(f"[Spawner] Injection manuelle peer: {room_id}")
    result = await peer_client.join_room(room_id)

    if not result:
        async with _lock:
            _active_rooms.discard(room_id)
        return {"status": "error", "room_id": room_id, "detail": "Peer join failed"}

    return {"status": "injected", "room_id": room_id}


async def eject_peer(room_id: str) -> dict:
    """
    Éjection manuelle du peer d'une room par un modérateur.
    Met à jour la config pour désactiver le peer.
    """
    await room_config_client.set_peer_enabled(room_id, False)

    async with _lock:
        if room_id not in _active_rooms:
            return {"status": "not_active", "room_id": room_id}
        _active_rooms.discard(room_id)

    log.info(f"[Spawner] Éjection manuelle peer: {room_id}")
    await peer_client.leave_room(room_id)
    return {"status": "ejected", "room_id": room_id}


async def set_peer_standby(room_id: str) -> dict:
    """
    Met le peer en mode figurant — présent dans la room mais silencieux.
    Il écoute mais n'intervient jamais.
    """
    async with httpx.AsyncClient(timeout=10) as c:
        pass  # handled via room config behavior_mode=silent

    from app.room_config_client import HEADERS
    import httpx
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.patch(
            f"{settings.ROOM_CONFIG_URL}/rooms/{room_id}",
            headers=HEADERS,
            json={"behavior_mode": "silent"},
        )
    log.info(f"[Spawner] Peer en veille (silent): {room_id}")
    return {"status": "standby", "room_id": room_id}


def get_active_rooms() -> list[str]:
    return list(_active_rooms)
