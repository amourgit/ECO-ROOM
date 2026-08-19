"""
OpenAIRealtimeEngine — implémentation `SpeechEngine` (app/speech/engine.py) pour l'API
Realtime d'OpenAI, cf. docs/architecture/05-gestionnaire-de-modeles.md §5.

**Groundé, pas deviné** : les événements et l'URL ci-dessous ont été vérifiés contre la
documentation officielle OpenAI au moment de l'écriture de ce module (endpoint WebSocket,
authentification, événements client/serveur GA de décembre 2025). Deux nuances documentées
explicitement plutôt que masquées :

  - Les noms des événements audio serveur ont changé entre la préversion
    (`response.audio.delta`) et la GA (`response.output_audio.delta`) — cette implémentation
    accepte les deux pour rester robuste face à un déploiement sur une version antérieure de
    l'API, sans deviner de troisième variante non observée.
  - Tout paramètre de session non confirmé par la documentation consultée (ex: réglages fins
    de `turn_detection`) est laissé à la valeur par défaut du serveur plutôt que fixé
    arbitrairement — cf. `SPEECH_MODEL_EXTRA` (app/config.py) pour surcharger explicitement si
    besoin, sans modifier ce fichier.

Contrairement à Gemini Live (16kHz en entrée), l'API Realtime OpenAI attend et produit du PCM16
mono à **24kHz** dans les deux sens (cf. `input_sample_rate`/`output_sample_rate` ci-dessous) —
c'est précisément pour ce genre de différence entre fournisseurs que
`app/browser/driver.py` paramètre désormais `AUDIO_BRIDGE_JS` par les débits déclarés du
moteur de parole configuré, plutôt que de les figer en dur (doc 05 §5).
"""
import asyncio
import base64
import json
import logging
import uuid

import websockets

log = logging.getLogger(__name__)

REALTIME_WS_BASE = "wss://api.openai.com/v1/realtime"

# Variantes observées selon la version de l'API — cf. docstring de module.
_AUDIO_DELTA_EVENTS = {"response.output_audio.delta", "response.audio.delta"}
_AUDIO_TRANSCRIPT_DELTA_EVENTS = {
    "response.output_audio_transcript.delta", "response.audio_transcript.delta",
}
_AUDIO_TRANSCRIPT_DONE_EVENTS = {
    "response.output_audio_transcript.done", "response.audio_transcript.done",
}
_INPUT_TRANSCRIPT_DELTA_EVENTS = {"conversation.item.input_audio_transcription.delta"}
_INPUT_TRANSCRIPT_DONE_EVENTS = {"conversation.item.input_audio_transcription.completed"}


class OpenAIRealtimeEngine:
    """Implémentation `SpeechEngine` pour l'API Realtime OpenAI (WebSocket, GA)."""

    def __init__(self, room_id: str, system_instruction: str,
                 on_speech: callable, on_audio: callable,
                 on_transcription: callable, context_provider: callable = None,
                 model: str = "gpt-realtime-2.1", voice: str = "alloy",
                 api_key: str = "", extra: dict | None = None):
        self.room_id = room_id
        self.system_instruction = system_instruction
        self.on_speech = on_speech
        self.on_audio = on_audio
        self.on_transcription = on_transcription
        self.context_provider = context_provider
        self._model = model
        self._voice = voice
        self._api_key = api_key
        self._extra = extra or {}

        self._ws = None
        self._ready = asyncio.Event()
        self._running = False
        self._task: asyncio.Task | None = None

        self._input_buf: list[str] = []
        self._output_buf: list[str] = []
        self._current_turn_id: str | None = None

    # ── Contrat SpeechEngine (doc 05) ────────────────────────────────────────────────────
    @property
    def input_sample_rate(self) -> int:
        return 24000

    @property
    def output_sample_rate(self) -> int:
        return 24000

    async def start(self) -> None:
        if not self._api_key:
            raise RuntimeError(
                "OpenAIRealtimeEngine requiert SPEECH_MODEL_API_KEY (clé API OpenAI) — "
                "cf. docs/architecture/05-gestionnaire-de-modeles.md"
            )
        self._running = True
        self._task = asyncio.create_task(self._run_loop())
        await asyncio.wait_for(self._ready.wait(), timeout=20.0)
        log.info(f"[OpenAIRealtime:{self.room_id}] Prêt \u2713")

    async def _run_loop(self):
        backoff = 2
        while self._running:
            try:
                await self._run_session()
                backoff = 2
            except Exception as e:
                if not self._running:
                    break
                log.warning(f"[OpenAIRealtime:{self.room_id}] Reconnexion ({e})")
                self._ready.clear()
                self._ws = None
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30)

    async def _run_session(self):
        url = f"{REALTIME_WS_BASE}?model={self._model}"
        headers = {"Authorization": f"Bearer {self._api_key}"}
        async with websockets.connect(url, additional_headers=headers) as ws:
            self._ws = ws

            session_config = {
                "type": "realtime",
                "instructions": self.system_instruction,
                "voice": self._voice,
                "audio": {
                    "input": {"format": {"type": "audio/pcm", "rate": self.input_sample_rate}},
                    "output": {"format": {"type": "audio/pcm", "rate": self.output_sample_rate}},
                },
                **self._extra,
            }
            await ws.send(json.dumps({"type": "session.update", "session": session_config}))

            await self._inject_catchup_context(ws)

            self._ready.set()

            async for raw in ws:
                if not self._running:
                    break
                await self._handle_event(json.loads(raw))

    async def _handle_event(self, event: dict) -> None:
        etype = event.get("type", "")

        if etype in _AUDIO_DELTA_EVENTS:
            delta_b64 = event.get("delta", "")
            if delta_b64:
                await self.on_audio(base64.b64decode(delta_b64))

        elif etype in _AUDIO_TRANSCRIPT_DELTA_EVENTS:
            if self._current_turn_id is None:
                self._current_turn_id = event.get("response_id") or str(uuid.uuid4())
            self._output_buf.append(event.get("delta", ""))

        elif etype in _AUDIO_TRANSCRIPT_DONE_EVENTS:
            await self._flush("output")

        elif etype in _INPUT_TRANSCRIPT_DELTA_EVENTS:
            if self._current_turn_id is None:
                self._current_turn_id = event.get("item_id") or str(uuid.uuid4())
            self._input_buf.append(event.get("delta", ""))

        elif etype in _INPUT_TRANSCRIPT_DONE_EVENTS:
            await self._flush("input")

        elif etype == "response.done":
            await self._flush("output")
            self._current_turn_id = None

        elif etype == "error":
            log.warning(f"[OpenAIRealtime:{self.room_id}] Erreur serveur: {event.get('error')}")

    async def _flush(self, kind: str) -> None:
        buf = self._input_buf if kind == "input" else self._output_buf
        if not buf:
            return
        text = "".join(buf)
        buf.clear()
        turn_id = self._current_turn_id
        try:
            if kind == "input":
                await self.on_transcription(text, turn_id)
            else:
                await self.on_speech(text, turn_id)
        except Exception as e:
            log.error(f"[OpenAIRealtime:{self.room_id}] Callback {kind}: {e}")

    async def _inject_catchup_context(self, ws) -> None:
        """Équivalent du rattrapage mémoire de GeminiSession (app/speech/gemini_live.py) —
        injecté comme un item de conversation système, sans déclencher de réponse (pas de
        response.create), donc jamais vocalisé."""
        if not self.context_provider:
            return
        try:
            context = self.context_provider()
        except Exception as e:
            log.warning(f"[OpenAIRealtime:{self.room_id}] context_provider: {e}")
            return
        if not context:
            return
        await ws.send(json.dumps({
            "type": "conversation.item.create",
            "item": {
                "type": "message",
                "role": "system",
                "content": [{
                    "type": "input_text",
                    "text": (
                        "[MÉMOIRE INTERNE DE LA RÉUNION — NE PAS LIRE À VOIX HAUTE, "
                        "sers-t'en uniquement comme contexte]\n"
                        f"{context}\n[FIN DE LA MÉMOIRE INTERNE]"
                    ),
                }],
            },
        }))
        log.info(f"[OpenAIRealtime:{self.room_id}] Contexte de reprise injecté ({len(context)} car.)")

    async def send_audio(self, pcm: bytes) -> None:
        if not self._ws or not self._ready.is_set():
            return
        try:
            await self._ws.send(json.dumps({
                "type": "input_audio_buffer.append",
                "audio": base64.b64encode(pcm).decode(),
            }))
        except Exception:
            pass

    async def send_text(self, text: str) -> None:
        if not self._ready.is_set():
            await asyncio.wait_for(self._ready.wait(), timeout=10.0)
        if not self._ws:
            return
        try:
            await self._ws.send(json.dumps({
                "type": "conversation.item.create",
                "item": {"type": "message", "role": "user",
                         "content": [{"type": "input_text", "text": text}]},
            }))
            await self._ws.send(json.dumps({"type": "response.create"}))
        except Exception as e:
            log.error(f"[OpenAIRealtime:{self.room_id}] send_text: {e}")

    async def send_image(self, jpeg_b64: str, prompt: str = "") -> None:
        """
        Vision — non confirmée par la documentation consultée pour ce module au moment de
        l'écriture (le contenu `input_image` existe côté API mais son intégration précise dans
        un tour Realtime n'a pas été vérifiée ici). Lève explicitement plutôt que d'envoyer un
        payload deviné — cf. docstring de module, même principe que les outils P1 du catalogue
        (docs/architecture/02-catalogue-outils-agent.md §11) : ne jamais faire semblant.
        """
        raise NotImplementedError(
            "OpenAIRealtimeEngine.send_image — format à valider contre la documentation "
            "OpenAI avant implémentation, cf. docstring de ce module"
        )

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        if self._ws:
            try:
                await self._ws.close()
            except Exception:
                pass
