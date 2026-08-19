"""
SpeechEngine — interface (port) du moteur de parole, cf.
docs/architecture/01-architecture-cible-civitas-agent.md §10 et
docs/architecture/05-gestionnaire-de-modeles.md.

Plusieurs implémentations existent désormais (gestionnaire de modèles neutre, app/models/) :
GeminiLiveEngine (app/speech/gemini_live.py, fournisseur par défaut) et OpenAIRealtimeEngine
(app/models/speech/openai_realtime.py). Chacune fusionne VAD+ASR+génération de réponse+TTS en
une session duplex temps réel (choix assumé, cf. doc 00 §4.1) — l'interface ne présuppose pas
qu'un fournisseur futur fasse pareil, elle documente juste le contrat commun aux fournisseurs
actuels.
"""
from typing import Awaitable, Callable, Protocol

OnSpeech = Callable[[str, str | None], Awaitable[None]]         # (text, turn_id)
OnTranscription = Callable[[str, str | None], Awaitable[None]]  # (text, turn_id)
OnAudio = Callable[[bytes], Awaitable[None]]                    # pcm sortant


class SpeechEngine(Protocol):
    """Contrat minimal que toute implémentation du moteur de parole doit respecter."""

    @property
    def input_sample_rate(self) -> int:
        """Fréquence d'échantillonnage PCM attendue en entrée (Hz). Les fournisseurs
        diffèrent (Gemini Live : 16000 ; OpenAI Realtime GA : 24000) — cf. doc 05 §5. Consommé
        par app/browser/driver.py pour paramétrer AUDIO_BRIDGE_JS au lieu d'un débit figé en
        dur, condition nécessaire pour qu'un changement de fournisseur soit réellement
        transparent pour le reste du CIVITAS Agent."""
        ...

    @property
    def output_sample_rate(self) -> int:
        """Fréquence d'échantillonnage PCM produite en sortie (Hz)."""
        ...

    async def start(self) -> None: ...

    async def stop(self) -> None: ...

    async def send_audio(self, pcm: bytes) -> None:
        """Audio entrant (participants) — mono int16 à `input_sample_rate`, cf. doc 00 §4.1."""
        ...

    async def send_text(self, text: str) -> None:
        """Injecte un tour de conversation textuel (ex: réponse au chat)."""
        ...

    async def send_image(self, jpeg_b64: str, prompt: str) -> None:
        """Vision — cf. app/perception/vision.py. Les fournisseurs qui ne supportent pas la
        vision dans leur session temps réel peuvent lever NotImplementedError — le nœud `act`
        (app/graph/nodes/acting.py) traite déjà toute exception d'outil sans planter le
        graphe (doc 01 §9)."""
        ...
