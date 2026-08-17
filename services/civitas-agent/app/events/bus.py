"""
EventBus — PORTÉ DE services/peer/app/events/bus.py, sans modification fonctionnelle.

Ce module était déjà explicitement commenté "Architecture LangGraph-ready" dans l'ancien peer
(cf. docs/architecture/00-etat-des-lieux.md §5.2) — il devient ici la couche de normalisation
en amont du nœud `ingest_data_event` (app/graph/nodes/ingest.py) : chaque événement brut du
navigateur headless (app/browser/driver.py) est d'abord dispatché sur ce bus (handlers legacy :
speaker tracker, log, kafka, modération), PUIS transmis au graphe pour la décision de
raisonnement — les deux mécanismes coexistent, ils ne sont pas redondants : le bus fait de la
mise à jour rapide et locale (SpeakerTracker), le graphe fait de la décision.
"""
import asyncio
import logging
from typing import Awaitable, Callable

log = logging.getLogger(__name__)

EventHandler = Callable[[str, dict], Awaitable[None]]


class EventBus:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self._handlers: dict[str, list[EventHandler]] = {}
        self._wildcard: list[EventHandler] = []

    def register(self, event_type: str, handler: EventHandler):
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
        """Les erreurs d'un handler n'affectent pas les autres (ni, a fortiori, une autre room —
        il n'y a qu'une room possible dans ce process, cf. app/config.py)."""
        targets = self._handlers.get(event_type, []) + self._wildcard
        for handler in targets:
            try:
                await handler(event_type, data)
            except Exception as e:
                log.error(
                    f"[EventBus:{self.room_id}] Handler error on {event_type}: {e}",
                    exc_info=True,
                )

    def emit_nowait(self, event_type: str, data: dict):
        asyncio.create_task(self.emit(event_type, data))
