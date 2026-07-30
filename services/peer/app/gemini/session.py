import asyncio
import logging
from google import genai
from google.genai import types
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

MODEL = "models/gemini-2.5-flash-native-audio-preview-12-2025"
SILENCE = bytes(3200)


class GeminiSession:
    """
    Session Gemini Live avec reconnexion automatique.
    - Reçoit PCM 16kHz mono int16
    - Produit PCM 24kHz mono int16
    - Transcrit les participants et les réponses de l'agent
    """

    def __init__(self, room_id: str, system_instruction: str,
                 on_speech: callable, on_audio: callable,
                 on_transcription: callable, context_provider: callable = None):
        self.room_id = room_id
        self.system_instruction = system_instruction
        self.on_speech = on_speech
        self.on_audio = on_audio
        self.on_transcription = on_transcription
        # Callable synchrone (pas de I/O réseau) qui renvoie le texte de
        # rattrapage à injecter à chaque (re)connexion — cf. _run_session().
        self.context_provider = context_provider
        self._client = None
        self._session = None
        self._ready = asyncio.Event()
        self._running = False
        self._task = None
        self._hb_task = None

    async def start(self):
        self._client = genai.Client(
            http_options={"api_version": "v1beta", "timeout": 60},
            api_key=settings.GEMINI_API_KEY,
        )
        self._running = True
        self._task = asyncio.create_task(self._run_loop())
        await asyncio.wait_for(self._ready.wait(), timeout=20.0)
        log.info(f"[Gemini:{self.room_id}] Prêt ✓")

    async def _run_loop(self):
        while self._running:
            try:
                await self._run_session()
            except Exception as e:
                if not self._running:
                    break
                log.warning(f"[Gemini:{self.room_id}] Reconnexion ({e})")
                self._ready.clear()
                self._session = None
                await asyncio.sleep(2)

    async def _run_session(self):
        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            output_audio_transcription={},
            input_audio_transcription={},
            system_instruction=self.system_instruction,
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Aoede"
                    )
                )
            ),
        )
        async with self._client.aio.live.connect(
            model=MODEL, config=config
        ) as session:
            self._session = session
            self._ready.set()
            self._hb_task = asyncio.create_task(self._heartbeat(session))

            await self._inject_catchup_context(session)

            async for response in session.receive():
                if not self._running:
                    break
                if response.data:
                    await self.on_audio(response.data)
                if response.server_content:
                    sc = response.server_content
                    if sc.output_transcription and sc.output_transcription.text:
                        await self.on_speech(sc.output_transcription.text)
                    if sc.input_transcription and sc.input_transcription.text:
                        await self.on_transcription(sc.input_transcription.text)

        self._session = None
        if self._hb_task:
            self._hb_task.cancel()

    async def _inject_catchup_context(self, session):
        """
        Réinjecte la mémoire de la réunion à chaque (re)connexion — premier
        démarrage compris. Ne dépend d'aucun appel réseau externe (le
        provider lit une mémoire déjà en RAM côté PeerInstance) : ça reste
        donc fiable même si c'est justement une coupure réseau qui a
        provoqué la reconnexion Gemini.

        end_of_turn=False : ce n'est pas un tour de conversation, juste du
        contexte — on ne veut pas que Gemini se sente obligé de répondre à
        voix haute immédiatement après une reconnexion.
        """
        if not self.context_provider:
            return
        try:
            context = self.context_provider()
        except Exception as e:
            log.warning(f"[Gemini:{self.room_id}] context_provider: {e}")
            return
        if not context:
            return
        try:
            await session.send(
                input=(
                    "[MÉMOIRE INTERNE DE LA RÉUNION — NE PAS LIRE À VOIX HAUTE, "
                    "NE PAS COMMENTER, sers-t'en uniquement comme contexte pour "
                    "la suite de la conversation]\n"
                    f"{context}\n"
                    "[FIN DE LA MÉMOIRE INTERNE]"
                ),
                end_of_turn=False,
            )
            log.info(f"[Gemini:{self.room_id}] Contexte de reprise injecté ({len(context)} car.)")
        except Exception as e:
            log.warning(f"[Gemini:{self.room_id}] Échec injection contexte: {e}")

    async def _heartbeat(self, session):
        while self._running and self._session is session:
            try:
                await session.send(
                    input={"data": SILENCE, "mime_type": "audio/pcm;rate=16000"},
                    end_of_turn=False,
                )
                await asyncio.sleep(2.0)
            except (asyncio.CancelledError, Exception):
                break

    async def send_audio(self, pcm_16k: bytes):
        if self._session and self._ready.is_set():
            try:
                await self._session.send(
                    input={"data": pcm_16k, "mime_type": "audio/pcm;rate=16000"},
                    end_of_turn=False,
                )
            except Exception:
                pass

    async def send_text(self, text: str):
        if not self._ready.is_set():
            await asyncio.wait_for(self._ready.wait(), timeout=10.0)
        if self._session:
            try:
                await self._session.send(input=text, end_of_turn=True)
            except Exception as e:
                log.error(f"[Gemini:{self.room_id}] send_text: {e}")

    async def send_image(self, jpeg_b64: str, prompt: str = ""):
        if not self._ready.is_set():
            await asyncio.wait_for(self._ready.wait(), timeout=10.0)
        if not self._session:
            return
        try:
            import base64
            await self._session.send(
                input={"mime_type": "image/jpeg", "data": base64.b64decode(jpeg_b64)},
                end_of_turn=False,
            )
            await self._session.send(
                input=prompt or "Décris ce que tu vois en français.",
                end_of_turn=True,
            )
        except Exception as e:
            log.error(f"[Gemini:{self.room_id}] send_image: {e}")

    async def stop(self):
        self._running = False
        if self._hb_task:
            self._hb_task.cancel()
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
