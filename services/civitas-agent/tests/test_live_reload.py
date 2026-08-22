"""
Test du rechargement de configuration EN DIRECT — cf.
docs/architecture/04-plan-migration.md §Phase 2 "standby/activate en direct" et
app/main.py::admin_reload_config.

Ce test ne peut pas passer par une vraie requête HTTP `/admin/reload_config` (celle-ci vit
dans app/main.py, qui importe des dépendances lourdes indisponibles dans cet environnement de
test — Playwright, google-genai, aiokafka, websockets, cf. README.md §Tests). Il valide en
revanche directement le mécanisme dont dépend cette route pour avoir un effet réel : muter
`GraphDeps.room_config` EN PLACE (`dict.clear()` + `dict.update()`, exactement ce que fait
`admin_reload_config`) doit changer le comportement du graphe DÈS LA PROCHAINE invocation,
SANS jamais reconstruire ni recompiler le graphe — c'est la condition nécessaire et suffisante
pour que `/admin/reload_config` fonctionne, et c'est ce que ce test prouve.
"""
from unittest.mock import AsyncMock

import pytest
from langgraph.checkpoint.memory import MemorySaver

from app.context.store import ContextStore
from app.graph.build import build_graph
from app.graph.deps import GraphDeps
from app.state import initial_state

ROOM_ID = "test-room"


def make_deps() -> GraphDeps:
    room_config = {
        "agent_name": "CIVITAS",
        "behavior_mode": "on_call",
        "invocation_keywords": ["civitas"],
        "permissions": {
            "can_speak": True, "can_write_chat": True,
            "can_use_tools": True, "can_use_rag": False, "can_moderate": False,
        },
        "tools_allowed": [],
    }
    return GraphDeps(
        room_id=ROOM_ID, room_config=room_config, browser=AsyncMock(),
        speech_engine=AsyncMock(), tool_registry=AsyncMock(),
        context_store=ContextStore(ROOM_ID), kafka=AsyncMock(),
    )


@pytest.mark.asyncio
async def test_mutating_room_config_in_place_changes_behavior_without_rebuilding_graph():
    deps = make_deps()
    checkpointer = MemorySaver()
    graph = build_graph(deps, checkpointer)  # construit et compilé UNE SEULE FOIS
    cfg = {"configurable": {"thread_id": ROOM_ID}}
    await graph.aupdate_state(cfg, initial_state(ROOM_ID))

    message_event = {"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "CIVITAS, bonjour"},
    }}

    # 1. Avant rechargement : behavior_mode="on_call" — le mot-clé déclenche une réponse.
    result_before = await graph.ainvoke(message_event, config=cfg)
    assert result_before["route_decision"] == "respond"

    # 2. Simule EXACTEMENT ce que fait POST /admin/reload_config (app/main.py) : mutation EN
    #    PLACE du MÊME dict, jamais de réassignation `deps.room_config = {...}` (qui casserait
    #    la référence partagée avec le graphe déjà compilé).
    deps.room_config.clear()
    deps.room_config.update({
        "agent_name": "CIVITAS",
        "behavior_mode": "silent",   # <- changement injecté "en direct"
        "invocation_keywords": ["civitas"],
        "permissions": deps.room_config.get("permissions", {}) or {
            "can_speak": True, "can_write_chat": True, "can_use_tools": True,
            "can_use_rag": False, "can_moderate": False,
        },
        "tools_allowed": [],
    })

    # 3. Après rechargement, MÊME graphe compilé, AUCUNE reconstruction : le même message
    #    doit désormais être ignoré — la preuve que le nœud `route` relit bien la config à
    #    chaque invocation (cf. app/graph/nodes/routing.py) plutôt que de l'avoir figée à la
    #    construction du graphe.
    result_after = await graph.ainvoke(message_event, config=cfg)
    assert result_after["route_decision"] == "ignore", (
        "le rechargement en direct n'a eu aucun effet — routing.py capture-t-il encore "
        "behavior_mode une seule fois à la construction du graphe ?"
    )


@pytest.mark.asyncio
async def test_reactivating_after_silent_also_takes_effect_live():
    """Symétrique du test précédent — valide /moderator/activate après /moderator/standby."""
    deps = make_deps()
    deps.room_config["behavior_mode"] = "silent"
    checkpointer = MemorySaver()
    graph = build_graph(deps, checkpointer)
    cfg = {"configurable": {"thread_id": ROOM_ID}}
    await graph.aupdate_state(cfg, initial_state(ROOM_ID))

    message_event = {"incoming_event": {
        "domain": "data", "event_type": "MESSAGE_RECEIVED",
        "data": {"participantId": "p1", "name": "Alice", "text": "CIVITAS, bonjour"},
    }}

    result_silent = await graph.ainvoke(message_event, config=cfg)
    assert result_silent["route_decision"] == "ignore"

    deps.room_config["behavior_mode"] = "on_call"  # équivalent de /moderator/activate

    result_active = await graph.ainvoke(message_event, config=cfg)
    assert result_active["route_decision"] == "respond"
