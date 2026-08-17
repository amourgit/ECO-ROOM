"""
kafka_consumer — ADAPTÉ DE services/room-spawner/app/kafka_consumer.py. Même sémantique :
seul consumer group sur `jitsi.room.events`/`jitsi.participant.events`, offset committé
uniquement après traitement réussi (at-least-once, cf. docs/architecture/00-etat-des-lieux.md
§3), backoff exponentiel de reconnexion sur le modèle déjà en place dans
app/kafka producer/producer du CIVITAS Agent (cf. services/civitas-agent/app/kafka/producer.py).

Seule différence de fond avec l'ancien room-spawner : le handler appelé pour chaque événement
ne fait plus un appel HTTP à un service `peer` partagé — il déclenche spawn/forward/teardown
via app/registry.py + app/docker_runtime.py + app/forwarder.py (cf. app/main.py).
"""
import asyncio
import json
import logging
from typing import Awaitable, Callable

from aiokafka import AIOKafkaConsumer

from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

TOPICS = ["jitsi.room.events", "jitsi.participant.events"]
GROUP_ID = "civitas-orchestrator"

EventHandler = Callable[[dict], Awaitable[None]]


async def consume_forever(handler: EventHandler):
    backoff = 5
    while True:
        try:
            consumer = AIOKafkaConsumer(
                *TOPICS,
                bootstrap_servers=settings.KAFKA_BOOTSTRAP,
                group_id=GROUP_ID,
                value_deserializer=lambda v: json.loads(v.decode()),
                enable_auto_commit=False,
                auto_offset_reset="earliest",
            )
            await consumer.start()
            log.info(f"[KafkaConsumer] Connecté ✓ ({', '.join(TOPICS)})")
            backoff = 5
            try:
                async for msg in consumer:
                    try:
                        await handler(msg.value)
                        await consumer.commit()
                    except Exception as e:
                        log.error(f"[KafkaConsumer] Erreur traitement événement: {e}", exc_info=True)
                        # Pas de commit — l'événement sera rejoué (at-least-once, comportement
                        # inchangé depuis l'ancien room-spawner).
            finally:
                await consumer.stop()
        except Exception as e:
            log.warning(f"[KafkaConsumer] Connexion échouée ({e}) — retry dans {backoff}s")
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 30)
