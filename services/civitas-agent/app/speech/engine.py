"""
SpeechEngine — interface (port) du moteur de parole, cf.
docs/architecture/01-architecture-cible-civitas-agent.md §10.

Aujourd'hui, une seule implémentation existe (GeminiSession, app/speech/gemini_live.py), qui
fusionne VAD+ASR+génération de réponse+TTS en une session Gemini Live duplex (choix assumé,
cf. docs/architecture/00-etat-des-lieux.md §4.1). Cette interface ne change RIEN au
comportement actuel — elle documente juste le contrat pour qu'un pipeline décomposé (VAD/ASR/
TTS séparés) puisse être branché plus tard sans toucher au graphe LangGraph ni aux outils.
"""
from typing import Awaitable, Callable, Protocol

OnSpeech = Callable[[str, str | None], Awaitable[None]]         # (text, turn_id)
OnTranscription = Callable[[str, str | None], Awaitable[None]]  # (text, turn_id)
OnAudio = Callable[[bytes], Awaitable[None]]                    # pcm sortant


class SpeechEngine(Protocol):
    """Contrat minimal que toute implémentation du moteur de parole doit respecter."""

    async def start(self) -> None: ...

    async def stop(self) -> None: ...

    async def send_audio(self, pcm_16k: bytes) -> None:
        """Audio entrant (participants) — 16kHz mono int16, cf. doc 00 §4.1."""
        ...

    async def send_text(self, text: str) -> None:
        """Injecte un tour de conversation textuel (ex: réponse au chat)."""
        ...

    async def send_image(self, jpeg_b64: str, prompt: str) -> None:
        """Vision — cf. app/perception/vision.py."""
        ...
