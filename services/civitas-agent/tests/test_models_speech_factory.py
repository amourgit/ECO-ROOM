"""
Tests app/models/speech/factory.py — cf. docs/architecture/05-gestionnaire-de-modeles.md §2.

Contrairement au raisonnement (optionnel), le moteur de parole est indispensable au
fonctionnement de l'agent — la factory ne dégrade donc jamais silencieusement : un fournisseur
inconnu ou un SDK manquant lève une exception avec un message actionnable, plutôt qu'un None
qui laisserait l'agent démarrer sans moteur de parole.
"""
import pytest

from app.config import Settings
from app.models.speech.factory import build_speech_engine


def make_settings(**overrides) -> Settings:
    return Settings(ROOM_ID="room-1", **overrides)


def test_unknown_provider_raises_value_error():
    settings = make_settings(SPEECH_MODEL_PROVIDER="nimportequoi")
    with pytest.raises(ValueError, match="inconnu"):
        build_speech_engine(settings, room_id="room-1", system_instruction="",
                             on_speech=None, on_audio=None, on_transcription=None)


def test_gemini_live_missing_sdk_raises_clear_runtime_error():
    """google-genai n'est pas installé dans cet environnement de test — la factory doit lever
    une RuntimeError explicite plutôt qu'un ImportError brut incompréhensible."""
    settings = make_settings(SPEECH_MODEL_PROVIDER="gemini_live", SPEECH_MODEL_API_KEY="k")
    with pytest.raises(RuntimeError, match="google-genai"):
        build_speech_engine(settings, room_id="room-1", system_instruction="",
                             on_speech=None, on_audio=None, on_transcription=None)
