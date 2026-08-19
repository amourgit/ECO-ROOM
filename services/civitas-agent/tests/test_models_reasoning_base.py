"""
Tests app/models/reasoning/base.py — cf. docs/architecture/05-gestionnaire-de-modeles.md §4.
Fonctions pures, communes aux 3 implémentations de fournisseur (gemini/openai/anthropic) —
testées une seule fois ici plutôt que dans chaque module de fournisseur.
"""
from app.models.reasoning.base import build_prompt, parse_completion


def test_build_prompt_includes_only_implemented_tools():
    tools = [
        {"name": "chat_tools.send_chat", "capability": "can_write_chat", "implemented": True},
        {"name": "chat_tools.create_poll", "capability": "can_write_chat", "implemented": False},
    ]
    prompt = build_prompt("système", "contexte", tools, "message")
    assert "chat_tools.send_chat" in prompt
    assert "chat_tools.create_poll" not in prompt


def test_build_prompt_handles_empty_tool_list():
    prompt = build_prompt("système", "contexte", [], "message")
    assert "aucun outil disponible" in prompt


def test_parse_completion_valid_json():
    raw = '{"say": "bonjour", "tool_calls": [{"tool": "chat_tools.send_chat", "args": {"text": "x"}, "reason": "r"}]}'
    result = parse_completion(raw)
    assert result["say"] == "bonjour"
    assert len(result["tool_calls"]) == 1
    assert result["tool_calls"][0]["tool"] == "chat_tools.send_chat"


def test_parse_completion_strips_markdown_code_fence():
    raw = '```json\n{"say": null, "tool_calls": []}\n```'
    result = parse_completion(raw)
    assert result["say"] is None
    assert result["tool_calls"] == []


def test_parse_completion_never_raises_on_garbage():
    """Le point le plus important : une réponse de modèle mal formée ne doit JAMAIS faire
    planter le graphe (doc 01 §9, même philosophie que le reste du projet)."""
    result = parse_completion("ceci n'est pas du JSON du tout {{{")
    assert result == {"say": None, "tool_calls": []}


def test_parse_completion_ignores_tool_calls_without_tool_name():
    raw = '{"say": null, "tool_calls": [{"args": {}, "reason": "sans nom d\'outil"}]}'
    result = parse_completion(raw)
    assert result["tool_calls"] == []
