"""
CIVITAS — Jitsi Event Bridge v2
Reçoit les webhooks Prosody et publie sur Kafka avec enrichissement complet.
"""
import hmac
import json
import logging
from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, Request, HTTPException, Header
from aiokafka import AIOKafkaProducer

from config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
)
log = logging.getLogger(__name__)
settings = get_settings()

# Routing des events vers les bons topics
TOPIC_MAP = {
    "muc-room-created":              "jitsi.room.events",
    "muc-room-destroyed":            "jitsi.room.events",
    "muc-occupant-joined":           "jitsi.participant.events",
    "muc-occupant-left":             "jitsi.participant.events",
    "muc-message":                   "jitsi.chat.events",
    "occupant-affiliation-changed":  "jitsi.participant.events",
    "occupant-role-changed":         "jitsi.participant.events",
}

# État local des rooms — participants en temps réel
_room_state: dict[str, dict] = {}

producer: AIOKafkaProducer = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode(),
        key_serializer=lambda k: k.encode() if k else None,
    )
    await producer.start()
    log.info(f"Kafka connecté ✓ ({settings.KAFKA_BOOTSTRAP})")
    yield
    await producer.stop()


app = FastAPI(
    title="CIVITAS Jitsi Event Bridge v2",
    version="2.0.0",
    lifespan=lifespan,
)


def _get_room(room_id: str) -> dict:
    if room_id not in _room_state:
        _room_state[room_id] = {
            "room_id": room_id,
            "created_at": datetime.utcnow().isoformat(),
            "participants": {},
            "participant_count": 0,
        }
    return _room_state[room_id]


def _update_presence(room_id: str, occupant: str, nick: str,
                     role: str, affiliation: str, joined: bool):
    room = _get_room(room_id)
    if joined:
        room["participants"][occupant] = {
            "jid": occupant,
            "nick": nick or occupant.split("/")[-1],
            "role": role or "participant",
            "affiliation": affiliation or "none",
            "joined_at": datetime.utcnow().isoformat(),
        }
    else:
        room["participants"].pop(occupant, None)
    room["participant_count"] = len(room["participants"])
    room["updated_at"] = datetime.utcnow().isoformat()


def _build_presence_snapshot(room_id: str) -> dict:
    room = _get_room(room_id)
    return {
        "room_id": room_id,
        "participant_count": room["participant_count"],
        "participants": list(room["participants"].values()),
        "snapshot_at": datetime.utcnow().isoformat(),
    }


async def _publish_presence(room_id: str):
    """Publie un snapshot complet de la présence sur room.presence."""
    snapshot = _build_presence_snapshot(room_id)
    await producer.send(
        "room.presence",
        key=room_id,
        value={
            "event_type": "presence.snapshot",
            "room_id": room_id,
            "source": "jitsi-event-bridge",
            "timestamp": datetime.utcnow().isoformat(),
            **snapshot,
        },
    )


@app.post("/webhook")
async def webhook(
    request: Request,
    x_civitas_webhook_secret: str | None = Header(default=None),
):
    """
    Reçoit les événements MUC de Prosody (mod_muc_webhook, cf.
    jitsi/prosody-plugins-custom/mod_muc_webhook.lua).

    AVANT : aucune authentification — n'importe qui sur le réseau LAN
    pouvait POSTer directement ici et injecter de fausses rooms/participants
    dans tout le pipeline CIVITAS (le port 8100 est publié sur l'hôte, cf.
    docker-compose.yml). Cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md.
    Comparaison à temps constant (hmac.compare_digest) pour éviter une
    fuite d'information par timing sur le secret.
    """
    if not x_civitas_webhook_secret or not hmac.compare_digest(
        x_civitas_webhook_secret, settings.WEBHOOK_SECRET
    ):
        raise HTTPException(status_code=401, detail="Secret webhook invalide ou absent")

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="JSON invalide")

    event_type = body.get("event_name", "unknown")
    room_id = body.get("room_name") or body.get("room") or "unknown"
    occupant = body.get("occupant_jid") or body.get("jid") or ""
    nick = body.get("occupant_nick") or body.get("nick") or ""
    role = body.get("role") or ""
    affiliation = body.get("affiliation") or ""

    now = datetime.utcnow().isoformat()

    # Mise à jour de l'état local de présence
    if event_type == "muc-occupant-joined":
        _update_presence(room_id, occupant, nick, role, affiliation, joined=True)
    elif event_type == "muc-occupant-left":
        _update_presence(room_id, occupant, nick, role, affiliation, joined=False)
    elif event_type == "muc-room-destroyed":
        _room_state.pop(room_id, None)
    elif event_type == "occupant-role-changed":
        room = _get_room(room_id)
        if occupant in room["participants"]:
            room["participants"][occupant]["role"] = role

    # Snapshot présence actuel
    presence = _build_presence_snapshot(room_id)

    # Payload enrichi
    payload = {
        "event_type":        event_type,
        "room_id":           room_id,
        "timestamp":         now,
        "source":            "prosody",
        "data":              body,
        # Présence temps réel
        "presence": {
            "participant_count": presence["participant_count"],
            "participants":      presence["participants"],
        },
        # Détails de l'occupant concerné
        "occupant": {
            "jid":         occupant,
            "nick":        nick,
            "role":        role,
            "affiliation": affiliation,
        } if occupant else None,
    }

    # Publier sur le topic principal
    topic = TOPIC_MAP.get(event_type, "jitsi.room.events")
    await producer.send(topic, key=room_id, value=payload)

    # Publier snapshot présence séparément pour tous les events participants
    if event_type in ("muc-occupant-joined", "muc-occupant-left",
                       "occupant-role-changed", "occupant-affiliation-changed"):
        await _publish_presence(room_id)

    log.info(
        f"[{event_type}] room={room_id} "
        f"participants={presence['participant_count']} → {topic}"
    )
    return {"status": "ok", "topic": topic, "event": event_type}


@app.get("/rooms")
async def list_rooms():
    """État temps réel de toutes les rooms actives."""
    return {
        "rooms": [
            _build_presence_snapshot(room_id)
            for room_id in _room_state
        ],
        "total_rooms": len(_room_state),
        "total_participants": sum(
            r["participant_count"] for r in _room_state.values()
        ),
    }


@app.get("/rooms/{room_id}")
async def get_room(room_id: str):
    """État temps réel d'une room spécifique."""
    if room_id not in _room_state:
        raise HTTPException(status_code=404, detail="Room inconnue")
    return _build_presence_snapshot(room_id)


@app.get("/health")
async def health():
    return {
        "service": "jitsi-event-bridge",
        "version": "2.0.0",
        "status": "ok",
        "active_rooms": len(_room_state),
        "kafka": settings.KAFKA_BOOTSTRAP,
    }
