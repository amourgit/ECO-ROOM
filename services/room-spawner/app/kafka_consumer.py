import asyncio
import json
import logging
from aiokafka import AIOKafkaConsumer
from app.config import get_settings
from app import spawner

settings = get_settings()
log = logging.getLogger(__name__)

TOPICS = ["jitsi.room.events", "jitsi.participant.events"]


async def start_consumer():
    consumer = AIOKafkaConsumer(
        *TOPICS,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP,
        group_id="civitas-room-spawner",
        auto_offset_reset="latest",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    await consumer.start()
    log.info(f"[KafkaConsumer] Connecté — topics: {TOPICS}")

    try:
        async for msg in consumer:
            await handle_event(msg.value)
    except asyncio.CancelledError:
        pass
    finally:
        await consumer.stop()
        log.info("[KafkaConsumer] Arrêté")


async def handle_event(event: dict):
    event_type = event.get("event_type", "")
    room_id = event.get("room_id", "")

    if not room_id or room_id == "unknown":
        return

    log.debug(f"[KafkaConsumer] Event: {event_type} — room: {room_id}")

    if event_type == "muc-room-created":
        await spawner.on_room_created(room_id)

    elif event_type == "muc-room-destroyed":
        await spawner.on_room_destroyed(room_id)
