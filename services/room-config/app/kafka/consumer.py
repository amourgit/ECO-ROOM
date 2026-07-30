"""
HistoryConsumer — persiste durablement le topic `room.transcriptions`.

Rôle unique : chaque interaction de réunion (parole participant transcrite,
parole agent, message chat) publiée par `peer` sur Kafka est écrite dans
Postgres (room_history_entries), indépendamment de la disponibilité ou du
cycle de vie du service `peer`.

Résilience :
  - Reconnexion infinie avec backoff exponentiel (jamais d'abandon définitif —
    contrairement au producer historique du peer, qui abandonnait après
    10 tentatives).
  - `enable_auto_commit=False` : l'offset n'est commité qu'après écriture DB
    réussie. En cas de crash entre les deux, le message est retraité au
    redémarrage (at-least-once — un doublon occasionnel est possible et
    acceptable, la perte de données ne l'est pas).
  - Un message malformé (JSON invalide, champs requis absents) est journalisé
    et l'offset commité quand même : le retraiter indéfiniment ne le
    réparerait pas et bloquerait tous les messages suivants de la partition.
  - Une erreur transitoire (DB indisponible, etc.) n'est PAS commitée : on
    se déconnecte et on retente — le message sera rejoué.
"""
import asyncio
import json
import logging
from datetime import datetime

from aiokafka import AIOKafkaConsumer
from app.config import get_settings
from app.database import SessionLocal
from app.services import room_history_service as history_svc

settings = get_settings()
log = logging.getLogger(__name__)

TOPIC = "room.transcriptions"
GROUP_ID = "civitas-room-history"
MAX_BACKOFF_SEC = 30

_task: asyncio.Task | None = None
_running = False


def _persist_sync(payload: dict) -> None:
    """Écriture DB synchrone — appelée via asyncio.to_thread (SQLAlchemy est sync ici)."""
    db = SessionLocal()
    try:
        occurred_at = None
        published_at = payload.get("published_at")
        if published_at:
            try:
                occurred_at = datetime.fromisoformat(published_at)
            except ValueError:
                occurred_at = None

        extra = payload.get("extra")
        history_svc.add_entry(
            db,
            room_id=payload["room_id"],
            speaker_name=payload.get("speaker") or "Inconnu",
            text=payload.get("text", ""),
            entry_type=payload.get("entry_type", "participant"),
            speaker_id=payload.get("speaker_id"),
            extra=extra if isinstance(extra, dict) else None,
            occurred_at=occurred_at,
        )
    finally:
        db.close()


def _is_valid(payload: dict) -> bool:
    return bool(payload.get("room_id")) and bool(payload.get("text", "").strip())


async def _consume_loop():
    global _running
    backoff = 2
    while _running:
        consumer = AIOKafkaConsumer(
            TOPIC,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            group_id=GROUP_ID,
            enable_auto_commit=False,
            auto_offset_reset="earliest",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )
        try:
            await consumer.start()
            log.info(f"[HistoryConsumer] Connecté ✓ (topic={TOPIC})")
            backoff = 2  # reset après connexion réussie

            async for msg in consumer:
                if not _running:
                    break
                payload = msg.value

                if not _is_valid(payload):
                    log.warning(f"[HistoryConsumer] Message ignoré (invalide): {payload}")
                    await consumer.commit()
                    continue

                try:
                    await asyncio.to_thread(_persist_sync, payload)
                    await consumer.commit()
                except Exception as e:
                    log.error(f"[HistoryConsumer] Échec persistance (DB ?) — {e}")
                    # Pas de commit : le message sera rejoué après reconnexion.
                    raise

        except asyncio.CancelledError:
            raise
        except Exception as e:
            log.warning(f"[HistoryConsumer] Erreur ({e}) — reconnexion dans {backoff}s")
        finally:
            try:
                await consumer.stop()
            except Exception:
                pass

        if _running:
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SEC)


async def start():
    global _task, _running
    if not settings.HISTORY_KAFKA_ENABLED:
        log.info("[HistoryConsumer] Désactivé (HISTORY_KAFKA_ENABLED=false)")
        return
    _running = True
    _task = asyncio.create_task(_consume_loop())
    log.info("[HistoryConsumer] Démarré ✓")


async def stop():
    global _running, _task
    _running = False
    if _task:
        _task.cancel()
        try:
            await _task
        except asyncio.CancelledError:
            pass
    log.info("[HistoryConsumer] Arrêté")
