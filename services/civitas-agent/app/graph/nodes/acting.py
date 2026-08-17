"""
act — doc 01 §6. Deux responsabilités, toutes deux déclenchées uniquement quand
`route_decision == "respond"` (cf. app/graph/build.py) :

  1. Déclenche le tour de réponse conversationnelle via le moteur de parole
     (`speech_engine.send_text`) — la fusion compréhension/génération/synthèse est interne à
     Gemini Live (doc 00 §4.1) ; ce nœud se contente de démarrer le tour, la livraison
     effective (audio vs. texte selon `response_mode`) est câblée dans app/main.py via les
     callbacks `on_speech`/`on_audio` du moteur de parole (cf. commentaire dans app/main.py).
  2. Exécute chaque `AgentAction` produite par `reason` (app/graph/nodes/reasoning.py), en
     passant SYSTÉMATIQUEMENT par `deps.tool_registry.invoke(...)` — jamais d'appel direct à
     un module `tools/*.py` — pour garantir que la vérification de permission
     (`room_configs.permissions`/`tools_allowed`, doc 01 §9) ne peut jamais être contournée.

Chaque outil exécuté (ou refusé) est journalisé dans `pending_actions` (accumulateur,
doc 01 §5/§6) — c'est la trace d'audit consommée par `persist`
(app/graph/nodes/persistence.py).
"""
from __future__ import annotations

import logging
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.state import ConferenceAgentState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]


def build_act(deps: GraphDeps) -> NodeFunc:
    async def act(state: ConferenceAgentState) -> dict:
        if state.get("route_decision") != "respond":
            return {}

        norm = state.get("normalized_event") or {}
        text = (norm.get("data") or {}).get("text", "")
        permissions = deps.room_config.get("permissions", {})
        tools_allowed = deps.room_config.get("tools_allowed", [])

        # 1. Réponse conversationnelle — cf. docstring de module.
        if text and permissions.get("can_speak", True):
            try:
                await deps.speech_engine.send_text(text)
            except Exception as e:
                log.error(f"[act:{deps.room_id}] send_text: {e}")

        # 2. Outils décidés par `reason`.
        executed = []
        for action in state.get("actions_to_execute", []):
            result = await deps.tool_registry.invoke(
                action["tool"], action["args"], permissions, tools_allowed,
                reason=action.get("reason", ""),
            )
            await deps.kafka.publish_agent_action(
                deps.room_id, action["tool"],
                {"args": action["args"], "reason": action.get("reason"), "result": result},
            )
            executed.append(action)

        return {"pending_actions": executed, "actions_to_execute": []}

    return act
