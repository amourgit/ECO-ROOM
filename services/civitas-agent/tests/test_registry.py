"""
Tests app/tools/registry.py — cœur de la modularité (doc 01 §9). Vérifie que
`room_configs.permissions`/`tools_allowed` sont réellement appliqués, et que le contrat de
sortie ({"ok", "allowed", "implemented", "result", "error"}) est stable — c'est le pattern
utilisé partout ailleurs (kick/mute historiques, doc 00 §5.4) généralisé à tous les outils.
"""
import pytest

from app.tools.registry import ToolRegistry, ToolSpec

PERMISSIVE = {"can_speak": True, "can_write_chat": True, "can_use_tools": True,
              "can_use_rag": True, "can_moderate": True}
RESTRICTIVE = {"can_speak": False, "can_write_chat": False, "can_use_tools": False,
                "can_use_rag": False, "can_moderate": False}


async def _ok_tool(**kwargs):
    return {"echo": kwargs}


async def _boom_tool(**kwargs):
    raise RuntimeError("kaboom")


def make_registry() -> ToolRegistry:
    r = ToolRegistry()
    r.register(ToolSpec(name="chat_tools.send_chat", func=_ok_tool, capability="can_write_chat"))
    r.register(ToolSpec(name="moderation_tools.kick_participant", func=_ok_tool, capability="can_moderate"))
    r.register(ToolSpec(name="presence_tools.raise_hand", func=_ok_tool, capability=None))
    r.register(ToolSpec(name="chat_tools.create_poll", func=_ok_tool, capability="can_write_chat", implemented=False))
    r.register(ToolSpec(name="tools.boom", func=_boom_tool, capability=None))
    return r


@pytest.mark.asyncio
async def test_unknown_tool_is_refused_cleanly():
    r = make_registry()
    result = await r.invoke("nope.does_not_exist", {}, PERMISSIVE, [])
    assert result["ok"] is False
    assert result["allowed"] is False
    assert result["implemented"] is False
    assert "inconnu" in result["error"]


@pytest.mark.asyncio
async def test_not_implemented_tool_never_pretends_success():
    r = make_registry()
    result = await r.invoke("chat_tools.create_poll", {}, PERMISSIVE, [])
    assert result["ok"] is False
    assert result["allowed"] is True          # la permission EST accordée...
    assert result["implemented"] is False      # ...mais l'outil n'existe pas encore (doc 02)


@pytest.mark.asyncio
async def test_capability_denied_blocks_call_before_it_happens():
    r = make_registry()
    result = await r.invoke("moderation_tools.kick_participant", {}, RESTRICTIVE, [])
    assert result["ok"] is False
    assert result["allowed"] is False
    assert "can_moderate" in result["error"]


@pytest.mark.asyncio
async def test_can_use_tools_gate_applies_when_capability_is_none():
    """presence_tools.raise_hand n'a pas de capability dédiée (doc 02 §2) — il reste soumis
    au garde-fou général can_use_tools (doc 01 §9)."""
    r = make_registry()
    result = await r.invoke("presence_tools.raise_hand", {}, RESTRICTIVE, [])
    assert result["allowed"] is False
    assert "can_use_tools" in result["error"]


@pytest.mark.asyncio
async def test_tools_allowed_whitelist_overrides_capability():
    r = make_registry()
    # can_moderate=True mais tools_allowed ne contient pas kick_participant → refusé quand
    # même (doc 01 §9 : "liste blanche explicite... prime sur les capacités générales").
    result = await r.invoke(
        "moderation_tools.kick_participant", {},
        PERMISSIVE, tools_allowed=["moderation_tools.mute_participant"],
    )
    assert result["allowed"] is False
    assert "tools_allowed" in result["error"]


@pytest.mark.asyncio
async def test_successful_invocation_returns_result():
    r = make_registry()
    result = await r.invoke("chat_tools.send_chat", {"text": "salut"}, PERMISSIVE, [])
    assert result["ok"] is True
    assert result["result"] == {"echo": {"text": "salut"}}


@pytest.mark.asyncio
async def test_exception_inside_tool_is_caught_and_reported():
    r = make_registry()
    result = await r.invoke("tools.boom", {}, PERMISSIVE, [])
    assert result["ok"] is False
    assert result["allowed"] is True
    assert result["implemented"] is True
    assert "kaboom" in result["error"]


def test_duplicate_registration_raises():
    r = make_registry()
    with pytest.raises(ValueError):
        r.register(ToolSpec(name="chat_tools.send_chat", func=_ok_tool, capability="can_write_chat"))


def test_describe_lists_all_tools_with_status():
    r = make_registry()
    described = r.describe()
    names = {d["name"] for d in described}
    assert "chat_tools.send_chat" in names
    poll = next(d for d in described if d["name"] == "chat_tools.create_poll")
    assert poll["implemented"] is False
