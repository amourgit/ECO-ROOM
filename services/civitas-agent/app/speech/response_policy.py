"""
Politique de réponse — PORTÉE DE services/peer/app/peer/response_policy.py, sans modification
fonctionnelle. Reste une fonction pure, testable isolément.

Utilisée par app/graph/nodes/routing.py (nœud `route`, cf.
docs/architecture/01-architecture-cible-civitas-agent.md §6) comme brique de décision de base
pour le mode `on_call` — le mode `proactive` (doc 01 §6.1) l'enrichit avec un jugement du nœud
`reason`, mais ne la remplace pas : cette fonction reste la référence pour "une sollicitation
vocale obtient toujours une réponse vocale, une sollicitation écrite obtient par défaut une
réponse écrite sauf demande explicite d'oral".
"""
from enum import Enum


class ResponseMode(str, Enum):
    AUDIO = "audio"
    TEXT = "text"


def parse_keywords(raw: str) -> list[str]:
    return [k.strip().lower() for k in raw.split(",") if k.strip()]


def decide_chat_response_mode(text: str, oral_keywords: list[str]) -> ResponseMode:
    text_lower = text.lower()
    if any(k in text_lower for k in oral_keywords):
        return ResponseMode.AUDIO
    return ResponseMode.TEXT
