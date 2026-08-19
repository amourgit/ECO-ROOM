"""
Factory du modèle de raisonnement — à partir de `Settings.REASONING_MODEL_*` (app/config.py).
Retourne `None` si non configuré (comportement par défaut : le nœud `reason` garde son
heuristique historique, doc 00 §5.6) — cf. docs/architecture/05-gestionnaire-de-modeles.md §4.
"""
import logging

from app.config import Settings
from app.models.reasoning.base import ReasoningModel

log = logging.getLogger(__name__)


def build_reasoning_model(settings: Settings) -> ReasoningModel | None:
    provider = settings.REASONING_MODEL_PROVIDER.strip().lower()
    if not provider:
        return None

    extra = settings.reasoning_model_extra()
    api_key = settings.REASONING_MODEL_API_KEY

    if not api_key:
        log.warning(
            f"[ReasoningFactory] REASONING_MODEL_PROVIDER='{provider}' configuré sans "
            f"REASONING_MODEL_API_KEY — raisonnement outillé désactivé, repli sur "
            f"l'heuristique (doc 00 §5.6)."
        )
        return None

    try:
        if provider == "gemini":
            from app.models.reasoning.gemini_text import DEFAULT_MODEL, GeminiReasoningModel
            return GeminiReasoningModel(
                api_key=api_key, model=settings.REASONING_MODEL_NAME or DEFAULT_MODEL, extra=extra,
            )

        if provider == "openai":
            from app.models.reasoning.openai_chat import DEFAULT_MODEL, OpenAIReasoningModel
            return OpenAIReasoningModel(
                api_key=api_key, model=settings.REASONING_MODEL_NAME or DEFAULT_MODEL, extra=extra,
            )

        if provider == "anthropic":
            from app.models.reasoning.anthropic_chat import (
                DEFAULT_MODEL,
                AnthropicReasoningModel,
            )
            return AnthropicReasoningModel(
                api_key=api_key, model=settings.REASONING_MODEL_NAME or DEFAULT_MODEL, extra=extra,
            )
    except ImportError as e:
        log.error(
            f"[ReasoningFactory] SDK manquant pour '{provider}' ({e}) — "
            f"cf. requirements.txt. Raisonnement outillé désactivé, repli sur l'heuristique."
        )
        return None

    log.warning(
        f"[ReasoningFactory] REASONING_MODEL_PROVIDER='{provider}' inconnu. Fournisseurs "
        f"supportés : 'gemini', 'openai', 'anthropic'. Repli sur l'heuristique."
    )
    return None
