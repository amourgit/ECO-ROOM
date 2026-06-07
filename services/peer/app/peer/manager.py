import asyncio
import logging
from app.peer.instance import PeerInstance

log = logging.getLogger(__name__)


class PeerManager:
    def __init__(self):
        self._instances: dict[str, PeerInstance] = {}

    async def create(self, room_id: str) -> PeerInstance:
        if room_id in self._instances:
            log.warning(f"[PeerManager] Instance déjà existante: {room_id}")
            return self._instances[room_id]

        instance = PeerInstance(room_id)
        self._instances[room_id] = instance
        try:
            await instance.start()
        except Exception as e:
            del self._instances[room_id]
            log.error(f"[PeerManager] Échec démarrage {room_id}: {e}")
            raise

        log.info(f"[PeerManager] Instance créée: {room_id} — total: {len(self._instances)}")
        return instance

    async def destroy(self, room_id: str):
        instance = self._instances.pop(room_id, None)
        if instance:
            await instance.stop()
            log.info(f"[PeerManager] Instance détruite: {room_id}")

    async def destroy_all(self):
        for room_id in list(self._instances.keys()):
            await self.destroy(room_id)

    def remove(self, room_id: str):
        self._instances.pop(room_id, None)

    def get(self, room_id: str) -> PeerInstance | None:
        return self._instances.get(room_id)

    def count(self) -> int:
        return len(self._instances)

    def list_active(self) -> list:
        return [
            {
                "room_id": r,
                "active": i.active,
                "agent_name": i.context.get("agent_name", "CIVITAS"),
                "behavior_mode": i.context.get("behavior_mode", "on_call"),
                "started_at": i.started_at.isoformat(),
                "duration_minutes": i.store.duration_minutes(),
            }
            for r, i in self._instances.items()
        ]


peer_manager = PeerManager()
