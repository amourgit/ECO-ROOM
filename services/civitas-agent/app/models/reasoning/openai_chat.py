"""
OpenAIReasoningModel — implémentation `ReasoningModel` via l'API Chat Completions standard
d'OpenAI (PAS l'API Realtime — distinct du moteur de parole,
app/models/speech/openai_realtime.py). Utilise `response_format={"type": "json_object"}`
(mode JSON strict natif d'OpenAI) plutôt que de dépendre uniquement de la consigne textuelle
partagée (app/models/reasoning/base.py) — une garantie supplémentaire propre à ce fournisseur.
"""
import logging

from app.models.reasoning.base import ReasoningCompletion, build_prompt, parse_completion

log = logging.getLogger(__name__)

DEFAULT_MODEL = "gpt-4o-mini"


class OpenAIReasoningModel:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, extra: dict | None = None):
        from openai import AsyncOpenAI

        self._client = AsyncOpenAI(api_key=api_key)
        self._model = model
        self._extra = extra or {}

    async def decide(
        self, *, system: str, context: str, available_tools: list[dict], user_message: str,
    ) -> ReasoningCompletion:
        prompt = build_prompt(system, context, available_tools, user_message)
        try:
            response = await self._client.chat.completions.create(
                model=self._model,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                **self._extra,
            )
            text = response.choices[0].message.content or ""
            return parse_completion(text)
        except Exception as e:
            log.error(f"[OpenAIReasoningModel] Échec: {e}")
            return ReasoningCompletion(say=None, tool_calls=[])
