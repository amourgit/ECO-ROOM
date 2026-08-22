"""
Tests app/room_config_client.py::is_agent_enabled — régression du bug de chemin de lecture
corrigé (cf. commentaire "Note de correction" dans app/room_config_client.py) : une première
version lisait `agent_enabled`/`peer_enabled` à la racine de la réponse `/context`, alors
qu'ils sont imbriqués sous `permissions` (AgentContextResponse, services/room-config). Sans
cette correction, `is_agent_enabled()` retombait systématiquement sur `True` par défaut, quoi
qu'un modérateur ait fait via `/moderator/eject` — exactement le bug historique déjà documenté
côté room-config pour `peer_enabled` avant sa propre correction.
"""
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.room_config_client import is_agent_enabled


def _mock_response(status_code: int, json_body: dict):
    resp = MagicMock()
    resp.status_code = status_code
    resp.json.return_value = json_body
    return resp


@pytest.mark.asyncio
async def test_reads_agent_enabled_from_nested_permissions_not_root():
    body = {"room_id": "r1", "permissions": {"agent_enabled": False, "peer_enabled": False}}
    with patch("httpx.AsyncClient.get", new=AsyncMock(return_value=_mock_response(200, body))):
        assert await is_agent_enabled("r1") is False


@pytest.mark.asyncio
async def test_agent_enabled_takes_priority_over_peer_enabled_when_both_present():
    body = {"permissions": {"agent_enabled": True, "peer_enabled": False}}
    with patch("httpx.AsyncClient.get", new=AsyncMock(return_value=_mock_response(200, body))):
        assert await is_agent_enabled("r1") is True


@pytest.mark.asyncio
async def test_falls_back_to_peer_enabled_when_agent_enabled_absent():
    """Coexistence des deux orchestrateurs (doc 04) : une room encore gérée uniquement via
    l'ancien peer_enabled (pas encore synchronisée) doit quand même être lue correctement."""
    body = {"permissions": {"peer_enabled": False}}
    with patch("httpx.AsyncClient.get", new=AsyncMock(return_value=_mock_response(200, body))):
        assert await is_agent_enabled("r1") is False


@pytest.mark.asyncio
async def test_defaults_to_true_when_neither_flag_present():
    body = {"permissions": {}}
    with patch("httpx.AsyncClient.get", new=AsyncMock(return_value=_mock_response(200, body))):
        assert await is_agent_enabled("r1") is True


@pytest.mark.asyncio
async def test_defaults_to_true_on_network_error():
    with patch("httpx.AsyncClient.get", new=AsyncMock(side_effect=Exception("boom"))):
        assert await is_agent_enabled("r1") is True


@pytest.mark.asyncio
async def test_defaults_to_true_on_non_200_status():
    with patch("httpx.AsyncClient.get", new=AsyncMock(return_value=_mock_response(404, {}))):
        assert await is_agent_enabled("r1") is True
