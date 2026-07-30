import asyncio
import json
import logging
from datetime import datetime

from aiokafka import AIOKafkaProducer
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

_producer: AIOKafkaProducer | None = None
_reconnect_task: asyncio.Task | None = None
_running = False


async def _connect_once() -> bool:
    global _producer
    try:
        producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            value_serializer=lambda v: json.dumps(v).encode(),
            key_serializer=lambda k: k.encode() if k else None,
        )
        await producer.start()
        _producer = producer
        log.info("[KafkaProducer] Connecté ✓")
        return True
    except Exception as e:
        log.warning(f"[KafkaProducer] Connexion échouée: {e}")
        _producer = None
        return False


async def _reconnect_loop():
    """
    Retente indéfiniment en arrière-plan, avec backoff, tant que non connecté.
    Sans ça, une indisponibilité Kafka au démarrage du peer tuait
    silencieusement et définitivement toute publication pour toute la durée
    de vie du process — donc une partie de l'historique de réunion perdue
    sans aucun signal.
    """
    backoff = 5
    while _running and not _producer:
        if await _connect_once():
            return
        await asyncio.sleep(backoff)
        backoff = min(backoff * 2, 30)


async def start():
    global _running
    _running = True
    # Quelques tentatives rapides et synchrones (cas nominal : Kafka déjà prêt),
    # puis on bascule en reconnexion de fond indéfinie si ça échoue encore.
    for attempt in range(5):
        if await _connect_once():
            return
        if attempt < 4:
            await asyncio.sleep(5)
    log.warning("[KafkaProducer] Toujours indisponible — reconnexion en arrière-plan")
    global _reconnect_task
    _reconnect_task = asyncio.create_task(_reconnect_loop())


async def stop():
    global _producer, _running, _reconnect_task
    _running = False
    if _reconnect_task:
        _reconnect_task.cancel()
        try:
            await _reconnect_task
        except asyncio.CancelledError:
            pass
    if _producer:
        await _producer.stop()
        _producer = None


async def publish(topic: str, key: str, payload: dict):
    if not _producer:
        return
    try:
        payload["published_at"] = datetime.utcnow().isoformat()
        await _producer.send(topic, key=key, value=payload)
    except Exception as e:
        log.warning(f"[KafkaProducer] {topic}: {e}")


async def publish_transcription(
    room_id: str,
    speaker: str,
    text: str,
    entry_type: str = "participant",
    speaker_id: str | None = None,
    extra: dict | None = None,
):
    payload = {
        "room_id": room_id, "speaker": speaker, "speaker_id": speaker_id,
        "text": text, "entry_type": entry_type, "source": "civitas-peer",
    }
    if extra:
        payload["extra"] = extra
    await publish("room.transcriptions", room_id, payload)


async def publish_agent_action(room_id: str, action: str, details: dict = {}):
    await publish("room.agent.actions", room_id, {
        "room_id": room_id, "action": action,
        "details": details, "source": "civitas-peer",
    })


async def publish_room_event(room_id: str, event_type: str, data: dict = {}):
    await publish("jitsi.room.events", room_id, {
        "room_id": room_id, "event_type": event_type,
        "data": data, "source": "civitas-peer",
    })


async def publish_participant_event(room_id: str, event_type: str, data: dict = {}):
    await publish("jitsi.participant.events", room_id, {
        "room_id": room_id, "event_type": event_type,
        "data": data, "source": "civitas-peer",
    })
