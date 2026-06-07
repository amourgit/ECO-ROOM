"""
EventBus — bus d'événements interne modulaire.

Architecture LangGraph-ready :
  - Chaque type d'événement Jitsi a son handler dédié
  - Les handlers sont enregistrables dynamiquement
  - Le bus dispatche vers tous les handlers abonnés
  - Chaque handler peut publier sur Kafka indépendamment

Usage :
    bus = EventBus(room_id)
    bus.register("USER_JOINED", my_handler)
    await bus.emit("USER_JOINED", {"participantId": "...", ...})
"""
import asyncio
import logging
from typing import Callable, Awaitable

log = logging.getLogger(__name__)

# Type d'un handler : async def handler(event_type: str, data: dict) -> None
EventHandler = Callable[[str, dict], Awaitable[None]]


class EventBus:
    def __init__(self, room_id: str):
        self.room_id   = room_id
        self._handlers: dict[str, list[EventHandler]] = {}
        self._wildcard: list[EventHandler]             = []  # handlers "*" (tout)

    def register(self, event_type: str, handler: EventHandler):
        """Enregistre un handler pour un type d'événement spécifique."""
        if event_type == "*":
            self._wildcard.append(handler)
        else:
            self._handlers.setdefault(event_type, []).append(handler)

    def unregister(self, event_type: str, handler: EventHandler):
        if event_type == "*":
            self._wildcard = [h for h in self._wildcard if h is not handler]
        else:
            self._handlers[event_type] = [
                h for h in self._handlers.get(event_type, []) if h is not handler
            ]

    async def emit(self, event_type: str, data: dict):
        """
        Dispatche un événement vers tous les handlers abonnés.
        Les erreurs d'un handler n'affectent pas les autres.
        """
        targets = self._handlers.get(event_type, []) + self._wildcard
        for handler in targets:
            try:
                await handler(event_type, data)
            except Exception as e:
                log.error(
                    f"[EventBus:{self.room_id}] Handler error "
                    f"on {event_type}: {e}",
                    exc_info=True
                )

    def emit_nowait(self, event_type: str, data: dict):
        """Version non-bloquante — crée une task asyncio."""
        asyncio.create_task(self.emit(event_type, data))
