import asyncio
import json
import logging
from datetime import datetime

from aiokafka import AIOKafkaProducer
from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

_producer: AIOKafkaProducer | None = None


async def start():
    global _producer
    max_retries = 10
    for attempt in range(max_retries):
        try:
            _producer = AIOKafkaProducer(
                bootstrap_servers=settings.KAFKA_BOOTSTRAP,
                value_serializer=lambda v: json.dumps(v).encode(),
                key_serializer=lambda k: k.encode() if k else None,
            )
            await _producer.start()
            log.info("[KafkaProducer] Connecté ✓")
            return
        except Exception as e:
            log.warning(f"[KafkaProducer] Tentative {attempt+1}/{max_retries} échouée: {e}")
            _producer = None
            if attempt < max_retries - 1:
                await asyncio.sleep(5)
    log.error("[KafkaProducer] Impossible de se connecter à Kafka — démarrage sans Kafka")


async def stop():
    global _producer
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


async def publish_transcription(room_id: str, speaker: str, text: str, entry_type: str = "participant"):
    await publish("room.transcriptions", room_id, {
        "room_id": room_id, "speaker": speaker,
        "text": text, "entry_type": entry_type, "source": "civitas-peer",
    })


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
