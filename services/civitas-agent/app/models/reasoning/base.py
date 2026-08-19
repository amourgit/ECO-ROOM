"""
ReasoningModel — interface (port) du modèle de raisonnement texte, cf.
docs/architecture/05-gestionnaire-de-modeles.md §4.

Distinct du SpeechEngine (app/speech/engine.py) : ce modèle ne parle jamais directement aux
participants — il décide, à partir de l'état de la conversation et du catalogue d'outils
disponibles (app/tools/registry.py), quel(s) outil(s) appeler. C'est le remplacement, quand il
est configuré, de l'heuristique par mot-clé du nœud `reason`
(app/graph/nodes/reasoning.py, doc 00 §5.6).

Convention commune aux 3 implémentations (gemini_text.py, openai_chat.py, anthropic_chat.py) :
prompt système + demande de sortie JSON stricte, parsée défensivement — une réponse mal
formée ne doit JAMAIS faire planter le graphe (doc 01 §9, même philosophie de dégradation
gracieuse que le reste du projet), elle produit simplement `tool_calls=[]`.
"""
from __future__ import annotations

import json
import logging
from typing import Protocol, TypedDict

log = logging.getLogger(__name__)


class ToolCallProposal(TypedDict):
    tool: str
    args: dict
    reason: str


class ReasoningCompletion(TypedDict):
    say: str | None
    tool_calls: list[ToolCallProposal]


class ReasoningModel(Protocol):
    async def decide(
        self, *, system: str, context: str, available_tools: list[dict], user_message: str,
    ) -> ReasoningCompletion:
        """
        `available_tools` provient de `ToolRegistry.describe()` — seuls les outils déjà
        déclarés dans le registre (donc déjà soumis au gating de permissions, doc 01 §9)
        peuvent être proposés ; le nœud `act` revérifie de toute façon les permissions avant
        tout appel réel, cf. app/graph/nodes/acting.py — cette interface ne fait AUCUNE
        confiance implicite au modèle de raisonnement.
        """
        ...


_JSON_INSTRUCTIONS = (
    "Réponds STRICTEMENT en JSON, sans texte avant ni après, avec ce schéma exact :\n"
    '{"say": "<texte à dire ou null>", '
    '"tool_calls": [{"tool": "<nom exact tiré de la liste d\'outils>", '
    '"args": {}, "reason": "<justification courte>"}]}\n'
    "Si aucun outil n'est pertinent, renvoie \"tool_calls\": []. "
    "N'invente jamais un nom d'outil hors de la liste fournie."
)


def build_prompt(system: str, context: str, available_tools: list[dict], user_message: str) -> str:
    tools_desc = "\n".join(
        f"- {t['name']}" + (f" (capacité requise: {t['capability']})" if t.get("capability") else "")
        for t in available_tools
        if t.get("implemented", True)
    ) or "(aucun outil disponible pour cette room)"

    return (
        f"{system}\n\n"
        f"Contexte récent de la réunion :\n{context}\n\n"
        f"Outils disponibles :\n{tools_desc}\n\n"
        f"Message à traiter : {user_message}\n\n"
        f"{_JSON_INSTRUCTIONS}"
    )


def parse_completion(raw_text: str) -> ReasoningCompletion:
    """
    Parsing défensif — jamais d'exception propagée. Tolère les blocs de code Markdown
    (```json ... ```) que certains modèles ajoutent malgré la consigne JSON stricte.
    """
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        data = json.loads(text)
        tool_calls = [
            ToolCallProposal(
                tool=str(tc.get("tool", "")),
                args=dict(tc.get("args") or {}),
                reason=str(tc.get("reason", "")),
            )
            for tc in (data.get("tool_calls") or [])
            if tc.get("tool")
        ]
        return ReasoningCompletion(say=data.get("say"), tool_calls=tool_calls)
    except (json.JSONDecodeError, AttributeError, TypeError) as e:
        log.warning(f"[ReasoningModel] Réponse non parsable, ignorée: {e} — texte: {raw_text[:200]!r}")
        return ReasoningCompletion(say=None, tool_calls=[])
