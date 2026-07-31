"""
Politique de réponse de l'agent — décide si une sollicitation doit obtenir
une réponse VOCALE (diffusée en direct dans la réunion) ou ÉCRITE (postée
dans le chat Jitsi).

Règle :
  - Une sollicitation VOCALE (audio participant capté par le micro) obtient
    TOUJOURS une réponse VOCALE — c'est le mode par défaut d'une réunion
    live, l'agent est un participant comme un autre.
  - Une sollicitation ÉCRITE (message chat) obtient PAR DÉFAUT une réponse
    ÉCRITE, pour ne jamais interrompre la réunion avec de l'audio non
    sollicité — SAUF si le message demande explicitement une réponse orale
    ("dis-le à voix haute", "réponds vocalement", ...), auquel cas l'agent
    peut répondre en audio même si la sollicitation était écrite.

Séparé de PeerInstance pour rester une fonction pure, testable isolément,
sans dépendre du reste de l'orchestration (browser, Gemini, Kafka...).
"""
from enum import Enum


class ResponseMode(str, Enum):
    AUDIO = "audio"  # réponse vocale, diffusée en direct dans la réunion
    TEXT = "text"     # réponse écrite dans le chat ; l'audio généré par
                       # Gemini est transcrit puis jamais diffusé aux participants


def parse_keywords(raw: str) -> list[str]:
    return [k.strip().lower() for k in raw.split(",") if k.strip()]


def decide_chat_response_mode(text: str, oral_keywords: list[str]) -> ResponseMode:
    text_lower = text.lower()
    if any(k in text_lower for k in oral_keywords):
        return ResponseMode.AUDIO
    return ResponseMode.TEXT
