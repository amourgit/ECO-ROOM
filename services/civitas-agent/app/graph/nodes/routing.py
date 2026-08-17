"""
route — doc 01 §6. Décide si l'événement qui vient de mettre à jour l'état appelle une
réaction du raisonnement (`reason` → éventuellement `act`/`speak`), ou peut être ignoré.

Réutilise app/speech/response_policy.py (porté tel quel, doc 00 §5.6) pour le choix
audio/texte — cette fonction reste la référence pour le mode `on_call`. Le mode `proactive`
(doc 01 §6.1) est amorcé ici par une heuristique simple et explicitement documentée comme
perfectible — la vraie valeur ajoutée du mode proactif viendra du nœud `reason` lui-même
(jugement LLM), pas d'une règle supplémentaire ici.

Important : les réactions de modération automatiques "légères" (ex: accuser réception d'une
main levée, signaler un micro coupé qui parle) restent gérées par app/events/handlers.py
(EventBus, hors graphe) — cf. doc 01 §8, ce module ne duplique pas cette logique. `route` ne
concerne QUE la décision de faire intervenir le raisonnement conversationnel.
"""
from __future__ import annotations

import logging
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.speech.response_policy import decide_chat_response_mode, parse_keywords
from app.state import ConferenceAgentState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]

_CONVERSATIONAL_KINDS = {"chat_message", "speech_transcript"}


def build_route(deps: GraphDeps) -> NodeFunc:
    keywords = [k.lower() for k in deps.room_config.get("invocation_keywords", ["civitas"])]
    oral_keywords = parse_keywords(deps.room_config.get(
        "oral_request_keywords",
        "oral,voix,parle,vocal,dis à voix,à voix haute,audio",
    ))
    behavior_mode = deps.room_config.get("behavior_mode", "on_call")

    async def route(state: ConferenceAgentState) -> dict:
        norm = state.get("normalized_event")
        if not norm or norm.get("silent"):
            return {"route_decision": "ignore"}

        if behavior_mode == "silent":
            return {"route_decision": "ignore"}

        if norm["kind"] not in _CONVERSATIONAL_KINDS:
            return {"route_decision": "ignore"}

        text = (norm.get("data") or {}).get("text", "")
        text_lower = text.lower()
        mentioned = any(k in text_lower for k in keywords)

        if not mentioned and behavior_mode != "proactive":
            return {"route_decision": "ignore"}

        if not mentioned and behavior_mode == "proactive":
            # Heuristique volontairement simple (doc 01 §6.1) : une question explicite sans
            # mention du nom peut mériter l'attention du raisonnement, qui décidera lui-même
            # s'il est pertinent d'intervenir (le nœud `reason` peut toujours choisir de ne
            # rien produire). Toute règle plus fine (silence prolongé, agenda non traité) est
            # un jugement du LLM, pas une règle supplémentaire ici — cf. doc 01 §6.1.
            if "?" not in text:
                return {"route_decision": "ignore"}

        response_mode = decide_chat_response_mode(text, oral_keywords).value
        return {"route_decision": "respond", "response_mode": response_mode}

    return route
