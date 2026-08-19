"""
reason — doc 01 §6. Ne s'exécute que lorsque `route_decision == "respond"` (cf. arête
conditionnelle dans app/graph/build.py).

Ce nœud ne génère PAS lui-même le texte de la réponse conversationnelle par défaut : dans
cette architecture, le moteur de parole (doc 00 §4.1, cf. app/models/speech/) fusionne déjà
compréhension + génération de réponse + synthèse vocale — c'est le nœud `act`
(app/graph/nodes/acting.py) qui déclenche ce tour via `speech_engine.send_text(...)`.

Le rôle de `reason` ici est de décider quels OUTILS (doc 02) doivent être appelés en
supplément de la réponse conversationnelle. Deux mécanismes, dans cet ordre :

  1. **Heuristique historique** (mot-clé de vision, doc 00 §5.6) — toujours active, coût nul,
     garde la parité fonctionnelle avec l'ancien `PeerInstance._handle_vision`.
  2. **Modèle de raisonnement outillé** (`deps.reasoning_model`, cf.
     app/models/reasoning/, doc 05 §4) — s'il est configuré (`REASONING_MODEL_PROVIDER`,
     app/config.py), vient compléter l'heuristique : il reçoit le catalogue d'outils
     réellement disponibles pour cette room (`deps.tool_registry.describe()`) et propose
     zéro, un ou plusieurs appels. **Aucune confiance implicite** : chaque proposition
     retraverse le gating de permissions du registre dans le nœud `act`
     (app/graph/nodes/acting.py) — un modèle de raisonnement mal configuré ou qui hallucine un
     nom d'outil ne peut jamais provoquer d'action non autorisée, au pire un refus loggé.

Si `deps.reasoning_model` est `None` (valeur par défaut, aucune variable `REASONING_MODEL_*`
renseignée), seule l'heuristique s'applique — comportement strictement identique à avant
l'introduction du gestionnaire de modèles neutre.
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
        text = (norm.get("data") or {}).get("text", "")
        text_lower = text.lower()
        actions: list[AgentAction] = []
        now = datetime.now(timezone.utc).isoformat()

        can_use_tools = deps.room_config.get("permissions", {}).get("can_use_tools", False)

        # 1. Heuristique historique (toujours active si can_use_tools) — cf. docstring §1.
        if can_use_tools and any(k in text_lower for k in _VISION_KEYWORDS):
            actions.append(AgentAction(
                tool="vision_tools.describe_screen",
                args={},
                reason="mot-clé de vision détecté dans le message — cf. doc 02 §7",
                requested_at=now,
            ))

        # 2. Modèle de raisonnement outillé, si configuré (doc 05 §4) — cf. docstring §2.
        if can_use_tools and deps.reasoning_model is not None and text:
            already_proposed = {a["tool"] for a in actions}
            try:
                context = deps.context_store.build_context(max_entries=20)
                completion = await deps.reasoning_model.decide(
                    system=deps.room_config.get("system_prompt", ""),
                    context=context,
                    available_tools=deps.tool_registry.describe(),
                    user_message=text,
                )
                for tc in completion.get("tool_calls", []):
                    if tc["tool"] in already_proposed:
                        continue  # déjà couvert par l'heuristique — pas de double exécution
                    actions.append(AgentAction(
                        tool=tc["tool"], args=tc.get("args", {}),
                        reason=tc.get("reason", "proposé par le modèle de raisonnement"),
                        requested_at=now,
                    ))
            except Exception as e:
                # Dégradation gracieuse (doc 00 §5.3) : un échec du modèle de raisonnement ne
                # doit jamais empêcher la réponse conversationnelle de base (nœud `act`).
                log.warning(f"[reason:{deps.room_id}] Échec du modèle de raisonnement: {e}")

        return {"actions_to_execute": actions}

    return reason
