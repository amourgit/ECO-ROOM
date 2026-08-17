"""
AgentRegistry — doc 03 §4.2. En mémoire, une entrée par room active. Une perte au redémarrage
de l'Orchestrateur n'est PAS une perte de données (cf. doc 03 §4.5 — reconstruction depuis
Docker au démarrage) : les containers agents survivent à l'Orchestrateur.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal, TypedDict

AgentStatus = Literal["starting", "healthy", "unhealthy", "stopping"]


class AgentHandle(TypedDict):
    room_id: str
    container_name: str
    base_url: str
    started_at: str
    status: AgentStatus


class AgentRegistry:
    def __init__(self):
        self._entries: dict[str, AgentHandle] = {}

    def get(self, room_id: str) -> AgentHandle | None:
        return self._entries.get(room_id)

    def put(self, handle: AgentHandle) -> None:
        self._entries[handle["room_id"]] = handle

    def remove(self, room_id: str) -> None:
        self._entries.pop(room_id, None)

    def set_status(self, room_id: str, status: AgentStatus) -> None:
        if room_id in self._entries:
            self._entries[room_id]["status"] = status

    def list_all(self) -> list[AgentHandle]:
        return list(self._entries.values())

    def is_active(self, room_id: str) -> bool:
        return room_id in self._entries


def make_handle(room_id: str, container_name: str, base_url: str) -> AgentHandle:
    return AgentHandle(
        room_id=room_id, container_name=container_name, base_url=base_url,
        started_at=datetime.now(timezone.utc).isoformat(), status="starting",
    )
