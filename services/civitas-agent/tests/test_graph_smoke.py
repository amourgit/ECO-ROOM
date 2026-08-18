"""
Test de fumée du graphe LangGraph assemblé (app/graph/build.py) — dépendances SIMULÉES
(browser, moteur de parole, Kafka) car aucun Jitsi/Gemini/Kafka réel n'est disponible dans cet
environnement (cf. tests/conftest.py). Utilise `MemorySaver` de LangGraph à la place du
`AsyncPostgresSaver` de production (app/graph/checkpoint.py) — suffisant pour valider que le
graphe s'assemble et s'exécute réellement (imports, signatures de nœuds, arêtes conditionnelles,
point d'entrée conditionnel), ce qu'aucune lecture de code ne peut garantir à elle seule.

Ce test est le critère concret qui distingue "le code compile" (déjà vérifié en Phase 0) de
"le graphe s'exécute et produit l'état attendu" (Phase 1, doc 04).
"""
from unittest.mock import AsyncMock

import pytest
from langgraph.checkpoint.memory import MemorySaver

from app.context.store import ContextStore
from app.graph.build import build_graph
from app.graph.deps import GraphDeps
from app.state import initial_state

ROOM_ID = "test-room"


def make_deps(**room_config_overrides) -> GraphDeps:
    room_config = {
        "agent_name": "CIVITAS",
        "behavior_mode": "on_call",
        "invocation_keywords": ["civitas"],
        "permissions": {
            "can_speak": True, "can_write_chat": True,
            "can_use_tools": True, "can_use_rag": False, "can_moderate": False,
        },
        "tools_allowed": [],
        **room_config_overrides,
    }
    return GraphDeps(
        room_id=ROOM_ID,
        room_config=room_config,
        browser=AsyncMock(),
        speech_engine=AsyncMock(),
        tool_registry=AsyncMock(),
        context_store=ContextStore(ROOM_ID),
        kafka=AsyncMock(),
    )


async def compiled_graph_with_state(deps: GraphDeps):
    checkpointer = MemorySaver()
    graph = build_graph(deps, checkpointer)
    cfg = {"configurable": {"thread_id": ROOM_ID}}
    await graph.aupdate_state(cfg, initial_state(ROOM_ID))
    return graph, cfg


@pytest.mark.asyncio
async def test_participant_joined_is_ignored_but_updates_participants():
    deps = make_deps()
    graph, cfg = await compiled_graph_with_state(deps)

    result = await graph.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "USER_JOINED",
        "data": {"participantId": "p1", "name": "Alice", "role": "participant"},
    }}, config=cfg)

    assert result["route_decision"] == "ignore"
    assert "p1" in result["participants"]
    assert result["participants"]["p1"]["display_name"] == "Alice"
    deps.speech_engine.send_text.assert_not_called()


@pytest.mark.asyncio
async def test_chat_message_without_invocation_keyword_is_ignored():
    deps = make_deps()
    graph, cfg = await compiled_graph_with_state(deps)

    result = await graph.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "bonjour tout le monde"},
    }}, config=cfg)

    assert result["route_decision"] == "ignore"
    deps.speech_engine.send_text.assert_not_called()


@pytest.mark.asyncio
async def test_chat_message_with_invocation_keyword_triggers_response():
    deps = make_deps()
    graph, cfg = await compiled_graph_with_state(deps)

    result = await graph.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "CIVITAS, quelle heure est-il ?"},
    }}, config=cfg)

    assert result["route_decision"] == "respond"
    deps.speech_engine.send_text.assert_awaited_once_with("CIVITAS, quelle heure est-il ?")
    # persist doit avoir publié la transcription (doc 01 §6)
    deps.kafka.publish_transcription.assert_awaited_once()
    # et la mémoire niveau 1 (ContextStore, vrai objet ici) doit contenir l'échange
    assert not deps.context_store.is_empty


@pytest.mark.asyncio
async def test_silent_mode_never_responds_even_with_keyword():
    deps = make_deps(behavior_mode="silent")
    graph, cfg = await compiled_graph_with_state(deps)

    result = await graph.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "CIVITAS, réponds !"},
    }}, config=cfg)

    assert result["route_decision"] == "ignore"
    deps.speech_engine.send_text.assert_not_called()


@pytest.mark.asyncio
async def test_vision_keyword_triggers_tool_via_registry_never_directly():
    deps = make_deps()
    deps.tool_registry.invoke.return_value = {"ok": True, "allowed": True, "implemented": True, "result": None, "error": None}
    graph, cfg = await compiled_graph_with_state(deps)

    result = await graph.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "CIVITAS, regarde l'écran"},
    }}, config=cfg)

    assert result["route_decision"] == "respond"
    deps.tool_registry.invoke.assert_awaited_once()
    called_tool_name = deps.tool_registry.invoke.call_args.args[0]
    assert called_tool_name == "vision_tools.describe_screen"
    # journal d'audit (doc 01 §6) alimenté avec l'action réellement exécutée
    assert any(a["tool"] == "vision_tools.describe_screen" for a in result["pending_actions"])


@pytest.mark.asyncio
async def test_room_id_isolation_between_two_independent_graphs():
    """Deux GraphDeps distincts (deux 'rooms' simulées dans le même process de test — en
    production ce sont deux process OS séparés, cf. doc 03) ne doivent jamais mélanger leurs
    ContextStore ou leurs mocks."""
    deps_a = make_deps()
    deps_a.room_id = "room-a"
    deps_b = make_deps()
    deps_b.room_id = "room-b"

    checkpointer = MemorySaver()
    graph_a = build_graph(deps_a, checkpointer)
    graph_b = build_graph(deps_b, checkpointer)

    cfg_a = {"configurable": {"thread_id": "room-a"}}
    cfg_b = {"configurable": {"thread_id": "room-b"}}
    await graph_a.aupdate_state(cfg_a, initial_state("room-a"))
    await graph_b.aupdate_state(cfg_b, initial_state("room-b"))

    await graph_a.ainvoke({"incoming_event": {
        "domain": "data", "event_type": "USER_JOINED",
        "data": {"participantId": "only-in-a", "name": "A"},
    }}, config=cfg_a)

    state_b = await graph_b.aget_state(cfg_b)
    assert "only-in-a" not in state_b.values["participants"]
