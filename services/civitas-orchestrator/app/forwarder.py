"""
forwarder — doc 03 §4.6. Un événement Kafka pour la room A n'est JAMAIS transmis physiquement
au process de la room B : le filtrage est fait une seule fois, ici, avant que l'information
n'atteigne le process de l'agent (cf. doc 03 §4.6 pour la justification complète).
"""
import logging

import httpx

from app.config import get_settings
from app.registry import AgentRegistry

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {"Authorization": f"Bearer {settings.AGENT_API_TOKEN}", "Content-Type": "application/json"}


async def forward_event(registry: AgentRegistry, event: dict) -> None:
    room_id = event.get("room_id")
    if not room_id:
        return
    handle = registry.get(room_id)
    if not handle:
        log.debug(f"[Forwarder] Aucun agent actif pour room={room_id} — événement ignoré")
        return
    try:
        async with httpx.AsyncClient(timeout=5) as c:
            await c.post(
                f"{handle['base_url']}/control/event",
                json={"room_id": room_id, "event_type": event.get("event_type"), "data": event.get("data", {})},
                headers=HEADERS,
            )
    except Exception as e:
        log.warning(f"[Forwarder] Échec forward vers {handle['container_name']}: {e}")
        registry.set_status(room_id, "unhealthy")
