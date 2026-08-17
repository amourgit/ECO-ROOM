"""
agent_client — remplace services/room-spawner/app/peer_client.py. Même contrat de sortie pour
compatibilité CLI (cf. docs/architecture/04-plan-migration.md), mais cible désormais
`handle["base_url"]` (un container précis) plutôt qu'un service partagé.
"""
import logging

import httpx

from app.config import get_settings
from app.registry import AgentHandle

settings = get_settings()
log = logging.getLogger(__name__)

HEADERS = {"Authorization": f"Bearer {settings.AGENT_API_TOKEN}", "Content-Type": "application/json"}


async def _post(handle: AgentHandle, path: str, json: dict | None = None) -> dict:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.post(f"{handle['base_url']}{path}", json=json or {}, headers=HEADERS)
        r.raise_for_status()
        return r.json()


async def _get(handle: AgentHandle, path: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{handle['base_url']}{path}", headers=HEADERS)
        r.raise_for_status()
        return r.json()


async def health(handle: AgentHandle) -> dict:
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{handle['base_url']}/health")
        return r.json()


async def send_text(handle: AgentHandle, text: str) -> dict:
    return await _post(handle, "/admin/send_text", {"text": text})


async def send_chat(handle: AgentHandle, text: str) -> dict:
    return await _post(handle, "/admin/send_chat", {"text": text})


async def kick(handle: AgentHandle, participant_id: str, reason: str | None = None) -> dict:
    return await _post(handle, "/admin/kick", {"participant_id": participant_id, "reason": reason})


async def mute(handle: AgentHandle, participant_id: str) -> dict:
    return await _post(handle, "/admin/mute", {"participant_id": participant_id})


async def moderator_status(handle: AgentHandle) -> dict:
    return await _get(handle, "/admin/moderator_status")


async def state(handle: AgentHandle) -> dict:
    return await _get(handle, "/admin/state")


async def shutdown(handle: AgentHandle) -> dict:
    return await _post(handle, "/shutdown")
