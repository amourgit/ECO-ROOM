"""
Tests app/models/reasoning/factory.py — cf. docs/architecture/05-gestionnaire-de-modeles.md §4.

Ces tests s'exécutent dans un environnement où aucun des SDK de fournisseur (google-genai,
openai, anthropic) n'est installé (cf. tests/conftest.py et le README du service) — c'est
précisément ce qui permet de valider, en conditions réelles et pas seulement en théorie, que
l'absence d'un SDK dégrade proprement vers `None` (repli sur l'heuristique, doc 00 §5.6)
plutôt que de faire planter le démarrage de l'agent.
"""
from app.config import Settings
from app.models.reasoning.factory import build_reasoning_model


def make_settings(**overrides) -> Settings:
    return Settings(GEMINI_API_KEY="dummy", **overrides)


def test_empty_provider_returns_none():
    assert build_reasoning_model(make_settings()) is None


def test_configured_provider_without_api_key_returns_none():
    settings = make_settings(REASONING_MODEL_PROVIDER="gemini", REASONING_MODEL_API_KEY="")
    assert build_reasoning_model(settings) is None


def test_unknown_provider_returns_none():
    settings = make_settings(REASONING_MODEL_PROVIDER="nimportequoi", REASONING_MODEL_API_KEY="k")
    assert build_reasoning_model(settings) is None


def test_missing_sdk_degrades_gracefully_instead_of_crashing():
    """Aucun SDK de fournisseur n'est installé dans cet environnement de test — la factory
    doit renvoyer None (jamais lever d'exception) et logguer clairement pourquoi."""
    for provider in ("gemini", "openai", "anthropic"):
        settings = make_settings(REASONING_MODEL_PROVIDER=provider, REASONING_MODEL_API_KEY="k")
        assert build_reasoning_model(settings) is None, f"provider={provider}"
