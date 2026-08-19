"""
GeminiReasoningModel — implémentation `ReasoningModel` (app/models/reasoning/base.py) via
l'API texte standard Gemini (`generate_content`, PAS Gemini Live — distinct du moteur de
parole, cf. docs/architecture/05-gestionnaire-de-modeles.md §4). Utilise le même SDK
`google-genai` déjà dépendance du projet (app/speech/gemini_live.py).
"""
import logging

from app.models.reasoning.base import ReasoningCompletion, build_prompt, parse_completion

log = logging.getLogger(__name__)

DEFAULT_MODEL = "gemini-2.5-flash"


class GeminiReasoningModel:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, extra: dict | None = None):
        from google import genai  # import différé — cf. openai_chat.py/anthropic_chat.py,
        # même convention : ne jamais exiger le SDK d'un fournisseur non sélectionné.

        self._client = genai.Client(api_key=api_key)
        self._model = model
        self._extra = extra or {}

    async def decide(
        self, *, system: str, context: str, available_tools: list[dict], user_message: str,
    ) -> ReasoningCompletion:
        prompt = build_prompt(system, context, available_tools, user_message)
        try:
            response = await self._client.aio.models.generate_content(
                model=self._model, contents=prompt,
            )
            return parse_completion(response.text or "")
        except Exception as e:
            log.error(f"[GeminiReasoningModel] Échec: {e}")
            return ReasoningCompletion(say=None, tool_calls=[])
