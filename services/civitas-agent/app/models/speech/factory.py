"""
Factory du moteur de parole — seul point du code qui décide quel fournisseur instancier,
à partir de `Settings.SPEECH_MODEL_*` (app/config.py). Cf.
docs/architecture/05-gestionnaire-de-modeles.md §2.

app/main.py n'importe jamais `GeminiSession` ni `OpenAIRealtimeEngine` directement — il appelle
`build_speech_engine(...)`, ce qui garantit qu'ajouter un nouveau fournisseur ne nécessite
aucune modification de app/main.py (doc 05 §6, point d'extension).
"""
import logging

from app.config import Settings
from app.speech.engine import SpeechEngine

log = logging.getLogger(__name__)


def build_speech_engine(
    settings: Settings,
    room_id: str,
    system_instruction: str,
    on_speech,
    on_audio,
    on_transcription,
    context_provider=None,
) -> SpeechEngine:
    provider = settings.SPEECH_MODEL_PROVIDER.strip().lower()
    extra = settings.speech_model_extra()

    if provider == "gemini_live":
        try:
            from app.speech.gemini_live import MODEL as GEMINI_DEFAULT_MODEL
            from app.speech.gemini_live import GeminiSession
        except ImportError as e:
            raise RuntimeError(
                f"SPEECH_MODEL_PROVIDER='gemini_live' requiert le paquet 'google-genai' "
                f"(cf. requirements.txt) — import échoué: {e}"
            ) from e

        if not settings.SPEECH_MODEL_API_KEY:
            raise RuntimeError(
                "SPEECH_MODEL_API_KEY (ou l'ancien GEMINI_API_KEY) est requis pour le "
                "fournisseur 'gemini_live' — cf. docs/architecture/05-gestionnaire-de-modeles.md"
            )
        # NB : GeminiSession lit sa clé API via app.config.get_settings() en interne
        # aujourd'hui (héritage direct du portage depuis services/peer, cf. doc 04 Phase 1) —
        # cohérent tant que SPEECH_MODEL_API_KEY est bien repris en repli de GEMINI_API_KEY.
        return GeminiSession(
            room_id=room_id,
            system_instruction=system_instruction,
            on_speech=on_speech,
            on_audio=on_audio,
            on_transcription=on_transcription,
            context_provider=context_provider,
            model=settings.SPEECH_MODEL_NAME or GEMINI_DEFAULT_MODEL,
            voice=settings.SPEECH_MODEL_VOICE or "Aoede",
        )

    if provider == "openai_realtime":
        try:
            from app.models.speech.openai_realtime import OpenAIRealtimeEngine
        except ImportError as e:
            raise RuntimeError(
                f"SPEECH_MODEL_PROVIDER='openai_realtime' requiert le paquet 'websockets' "
                f"(cf. requirements.txt) — import échoué: {e}"
            ) from e

        return OpenAIRealtimeEngine(
            room_id=room_id,
            system_instruction=system_instruction,
            on_speech=on_speech,
            on_audio=on_audio,
            on_transcription=on_transcription,
            context_provider=context_provider,
            model=settings.SPEECH_MODEL_NAME or "gpt-realtime-2.1",
            voice=settings.SPEECH_MODEL_VOICE or "alloy",
            api_key=settings.SPEECH_MODEL_API_KEY,
            extra=extra,
        )

    raise ValueError(
        f"SPEECH_MODEL_PROVIDER='{provider}' inconnu. Fournisseurs supportés : "
        f"'gemini_live', 'openai_realtime'. Pour en ajouter un, cf. "
        f"docs/architecture/05-gestionnaire-de-modeles.md §6."
    )
