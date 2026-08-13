"""
Consumer Kafka — room-spawner.

Écoute jitsi.room.events / jitsi.participant.events et déclenche
l'instanciation/l'éjection automatique du peer.

Résilience (cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §2.2b/§5 Phase 2) :
  AVANT : `auto_offset_reset="latest"` + auto-commit implicite. Un
  redémarrage de ce service (déploiement, crash) ratait DÉFINITIVEMENT tout
  événement `muc-room-created` transité entre-temps — "latest" signifie
  "ignore tout ce qui existe déjà dans le topic, commence à partir de
  maintenant". Combiné à l'auto-commit (qui avance l'offset même si
  `handle_event` a levé une exception), un simple crash pendant le
  traitement pouvait aussi faire sauter un événement sans jamais le rejouer.

  MAINTENANT : `auto_offset_reset="earliest"` + `enable_auto_commit=False`,
  offset commité uniquement après traitement réussi — même pattern déjà en
  place pour le HistoryConsumer de room-config (app/kafka/consumer.py) :
  au redémarrage, tout ce qui a été manqué est rattrapé (at-least-once — un
  doublon occasionnel est possible et sans risque ici, `on_room_created`
  est déjà idempotent via `_active_rooms`, jamais de perte silencieuse
  acceptée). Reconnexion infinie avec backoff exponentiel en cas de coupure
  Kafka, alignée sur le même principe.
"""
import asyncio
import json
import logging
from aiokafka import AIOKafkaConsumer
from app.config import get_settings
from app import spawner

settings = get_settings()
log = logging.getLogger(__name__)

TOPICS = ["jitsi.room.events", "jitsi.participant.events"]
GROUP_ID = "civitas-room-spawner"
MAX_BACKOFF_SEC = 30

_running = False


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


async def start_consumer():
    global _running
    _running = True
    backoff = 2

    while _running:
        consumer = AIOKafkaConsumer(
            *TOPICS,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            group_id=GROUP_ID,
            enable_auto_commit=False,
            auto_offset_reset="earliest",
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )
        try:
            await consumer.start()
            log.info(f"[KafkaConsumer] Connecté ✓ — topics: {TOPICS}")
            backoff = 2  # reset après connexion réussie

            async for msg in consumer:
                if not _running:
                    break
                try:
                    await handle_event(msg.value)
                    await consumer.commit()
                except Exception as e:
                    log.error(
                        f"[KafkaConsumer] Échec traitement événement "
                        f"(room={msg.value.get('room_id')}) — {e}",
                        exc_info=True,
                    )
                    # Pas de commit : rejoué après reconnexion (at-least-once).
                    raise

        except asyncio.CancelledError:
            raise
        except Exception as e:
            log.warning(f"[KafkaConsumer] Erreur ({e}) — reconnexion dans {backoff}s")
        finally:
            try:
                await consumer.stop()
            except Exception:
                pass

        if _running:
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SEC)

    log.info("[KafkaConsumer] Arrêté")


def stop_consumer():
    global _running
    _running = False
