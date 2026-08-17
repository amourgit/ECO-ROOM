"""
build.py — assemble le graphe LangGraph décrit en doc 01 §6 :

    (entrée conditionnelle selon incoming_event["domain"])
      "control" → ingest_control_event ─┐
      "data"    → ingest_data_event ────┴─→ update_state → route ──┬─(ignore)─→ END
                                                                     └─(respond)─→ reason → act → persist → END

Un seul graphe compilé par process (donc par room, cf. app/config.py) — jamais partagé.
"""
from __future__ import annotations

import logging
from typing import Literal

from langgraph.graph import END, StateGraph

from app.graph.deps import GraphDeps
from app.graph.nodes.acting import build_act
from app.graph.nodes.ingest import build_ingest_control, build_ingest_data
from app.graph.nodes.persistence import build_persist
from app.graph.nodes.reasoning import build_reason
from app.graph.nodes.routing import build_route
from app.graph.nodes.state_update import build_update_state
from app.state import ConferenceAgentState

log = logging.getLogger(__name__)


def _entry_router(state: ConferenceAgentState) -> Literal["control", "data"]:
    event = state.get("incoming_event") or {}
    return "control" if event.get("domain") == "control" else "data"


def _route_decision_router(state: ConferenceAgentState) -> Literal["respond", "ignore"]:
    return "respond" if state.get("route_decision") == "respond" else "ignore"


def build_graph(deps: GraphDeps, checkpointer):
    """
    Compile le graphe pour CETTE room (deps.room_id). `checkpointer` provient de
    app/graph/checkpoint.py (build_checkpointer) — thread_id = deps.room_id garanti par
    app/main.py au moment de l'invocation (checkpoint.thread_config).
    """
    graph = StateGraph(ConferenceAgentState)

    graph.add_node("ingest_control_event", build_ingest_control(deps))
    graph.add_node("ingest_data_event", build_ingest_data(deps))
    graph.add_node("update_state", build_update_state(deps))
    graph.add_node("route", build_route(deps))
    graph.add_node("reason", build_reason(deps))
    graph.add_node("act", build_act(deps))
    graph.add_node("persist", build_persist(deps))

    graph.set_conditional_entry_point(
        _entry_router,
        {"control": "ingest_control_event", "data": "ingest_data_event"},
    )

    graph.add_edge("ingest_control_event", "update_state")
    graph.add_edge("ingest_data_event", "update_state")
    graph.add_edge("update_state", "route")

    graph.add_conditional_edges(
        "route", _route_decision_router,
        {"respond": "reason", "ignore": END},
    )

    graph.add_edge("reason", "act")
    graph.add_edge("act", "persist")
    graph.add_edge("persist", END)

    compiled = graph.compile(checkpointer=checkpointer)
    log.info(f"[Graph:{deps.room_id}] Compilé \u2713 ({len(graph.nodes)} nœuds)")
    return compiled
