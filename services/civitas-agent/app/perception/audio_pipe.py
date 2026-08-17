"""
AudioPipe — PORTÉ DE services/peer/app/audio/pipe.py, sans modification fonctionnelle.

Pont audio WebSocket local entre Chrome headless (app/browser/driver.py) et le moteur de
parole (app/speech/gemini_live.py). Entrant : PCM 16kHz int16 depuis les participants (Web
Audio API). Sortant : PCM 24kHz int16 depuis le moteur de parole (voix de l'agent).

Le port WebSocket est dynamique et local (127.0.0.1) : aucun changement nécessaire pour
l'isolation par container, chaque container a son propre 127.0.0.1 (cf.
docs/architecture/03-isolation-et-orchestration.md §3).
"""
import asyncio
import logging

import websockets
from websockets.server import WebSocketServerProtocol

log = logging.getLogger(__name__)


class AudioPipe:
    def __init__(self, room_id: str, on_audio_in: callable):
        self.room_id = room_id
        self.on_audio_in = on_audio_in
        self._server = None
        self._ws: WebSocketServerProtocol | None = None
        self._port = 0
        self._connected = asyncio.Event()

    async def start(self) -> int:
        self._server = await websockets.serve(
            self._handle,
            host="127.0.0.1",
            port=0,
        )
        self._port = self._server.sockets[0].getsockname()[1]
        log.info(f"[AudioPipe:{self.room_id}] Port {self._port}")
        return self._port

    async def _handle(self, ws: WebSocketServerProtocol):
        self._ws = ws
        self._connected.set()
        log.info(f"[AudioPipe:{self.room_id}] Browser connecté ✓")
        try:
            async for msg in ws:
                if isinstance(msg, bytes) and len(msg) > 0:
                    await self.on_audio_in(msg)
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            self._ws = None
            self._connected.clear()
            log.info(f"[AudioPipe:{self.room_id}] Browser déconnecté")

    async def send_audio(self, pcm_24k: bytes):
        if self._ws:
            try:
                await self._ws.send(pcm_24k)
            except Exception:
                pass

    async def wait_connected(self, timeout: float = 20.0):
        await asyncio.wait_for(self._connected.wait(), timeout=timeout)

    async def stop(self):
        if self._server:
            self._server.close()
            await self._server.wait_closed()

    @property
    def port(self) -> int:
        return self._port
