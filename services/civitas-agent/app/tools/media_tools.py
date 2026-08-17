"""
media_tools — doc 02 §5. Enregistrement/transcription — requièrent can_moderate. Dépend de
Jibri configuré côté infra Jitsi (hors périmètre CIVITAS, cf. doc 02 §5).
"""
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="media_tools.start_recording",
        func=lambda mode="file", **options: browser.start_recording(mode, **options),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="media_tools.stop_recording",
        func=lambda mode="file": browser.stop_recording(mode),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="media_tools.get_transcription_status",
        func=lambda: browser.get_transcription_status(),
        capability=None, doc_status="📖",
    ))

    async def _not_implemented(**_kwargs):
        raise NotImplementedError(
            "streaming live — cf. doc 02 §5, gestion sécurisée de la clé de stream requise"
        )

    registry.register(ToolSpec(
        name="media_tools.start_streaming", func=_not_implemented,
        capability="can_moderate", implemented=False, doc_status="🔧",
    ))
