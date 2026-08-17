"""
Control Ingress — NOUVEAU (n'existe pas dans services/peer, qui consommait Kafka directement
en étant multi-room). Cf. docs/architecture/03-isolation-et-orchestration.md §4.6.

Ce process CIVITAS Agent ne consomme JAMAIS Kafka directement : civitas-orchestrator est
l'unique consumer group sur `jitsi.room.events`/`jitsi.participant.events`, et lui forwarde
uniquement les événements concernant CETTE room via un simple POST HTTP. C'est la garantie que
le Control Plane ne peut physiquement pas transporter l'événement d'une autre room jusqu'ici :
il n'y a même pas de client Kafka dans ce process pour un événement mal filtré à intercepter.

Ce module expose une file asyncio simple, consommée par la boucle principale du graphe
(app/main.py) — découplage volontaire entre "recevoir un événement HTTP" (rapide, ne doit
jamais bloquer sur le traitement) et "le traiter dans le graphe" (peut prendre plus de temps,
ex: un tour de raisonnement LLM).
"""
import asyncio
import logging

log = logging.getLogger(__name__)

# Une seule file, car un seul graphe tourne dans ce process (une seule room).
control_event_queue: asyncio.Queue[dict] = asyncio.Queue()


async def enqueue_control_event(event: dict) -> None:
    """
    Appelé par la route FastAPI POST /control/event (app/main.py). Ne fait aucune validation
    métier ici — la validation de forme minimale (room_id présent) est faite côté route ;
    la normalisation complète est la responsabilité du nœud `ingest_control_event`
    (app/graph/nodes/ingest.py), pas de ce module de transport.
    """
    await control_event_queue.put(event)
    log.debug(f"[ControlIngress] Événement mis en file: {event.get('event_type')}")
