"""
reason — doc 01 §6. Ne s'exécute que lorsque `route_decision == "respond"` (cf. arête
conditionnelle dans app/graph/build.py).

Ce nœud ne génère PAS lui-même le texte de la réponse conversationnelle : dans cette
architecture, le moteur de parole (Gemini Live, app/speech/gemini_live.py) fusionne déjà
compréhension + génération de réponse + synthèse vocale (doc 00 §4.1, doc 01 §4.1) — c'est le
nœud `act` (app/graph/nodes/acting.py) qui déclenche ce tour via `speech_engine.send_text(...)`.

Le rôle de `reason` ici est complémentaire et plus restreint, mais réel : décider quels OUTILS
(doc 02) doivent être appelés en supplément de la réponse conversationnelle — par exemple
déclencher `vision_tools.describe_screen` sur détection d'une intention visuelle. C'est la
même logique que l'ancien `PeerInstance._handle_vision` (déclenchement par mot-clé,
doc 00 §5.6), reprise ici comme un premier palier volontairement simple.

TODO (doc 04, au-delà de la Phase 1) : remplacer cette heuristique par un véritable appel LLM
à sorties structurées (tool-calling) qui choisit parmi `deps.tool_registry.describe()` sans
liste de mots-clés codée en dur — l'architecture (registre découplé du graphe, doc 01 §9) le
permet déjà sans changement de structure, seul le corps de cette fonction est à remplacer.
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.state import AgentAction, ConferenceAgentState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]

_VISION_KEYWORDS = ("regarde", "écran", "screenshot", "vois-tu", "partage d'écran")


def build_reason(deps: GraphDeps) -> NodeFunc:
    async def reason(state: ConferenceAgentState) -> dict:
        norm = state.get("normalized_event") or {}
        text = (norm.get("data") or {}).get("text", "").lower()
        actions: list[AgentAction] = []

        can_use_tools = deps.room_config.get("permissions", {}).get("can_use_tools", False)
        if can_use_tools and any(k in text for k in _VISION_KEYWORDS):
            actions.append(AgentAction(
                tool="vision_tools.describe_screen",
                args={},
                reason="mot-clé de vision détecté dans le message — cf. doc 02 §7",
                requested_at=datetime.now(timezone.utc).isoformat(),
            ))

        return {"actions_to_execute": actions}

    return reason
