"""
AnthropicReasoningModel — implémentation `ReasoningModel` via l'API Messages standard
d'Anthropic. Pas de mode JSON strict natif comme OpenAI (`response_format`) — repose donc
entièrement sur la consigne textuelle partagée (app/models/reasoning/base.py) et sur le
parsing défensif, qui tolère déjà les blocs ```json``` que Claude ajoute parfois malgré la
consigne.
"""
import logging

from app.models.reasoning.base import ReasoningCompletion, build_prompt, parse_completion

log = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-sonnet-4-6"


class AnthropicReasoningModel:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, extra: dict | None = None):
        from anthropic import AsyncAnthropic

        self._client = AsyncAnthropic(api_key=api_key)
        self._model = model
        self._extra = extra or {}

    async def decide(
        self, *, system: str, context: str, available_tools: list[dict], user_message: str,
    ) -> ReasoningCompletion:
        prompt = build_prompt(system, context, available_tools, user_message)
        extra = dict(self._extra)
        max_tokens = extra.pop("max_tokens", 1024)
        try:
            response = await self._client.messages.create(
                model=self._model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
                **extra,
            )
            text = "".join(
                block.text for block in response.content if getattr(block, "type", "") == "text"
            )
            return parse_completion(text)
        except Exception as e:
            log.error(f"[AnthropicReasoningModel] Échec: {e}")
            return ReasoningCompletion(say=None, tool_calls=[])
