"""
ingest_control_event / ingest_data_event — doc 01 §6.

Normalisent l'événement brut transitoire (`state["incoming_event"]`, posé par app/main.py à
chaque invocation du graphe) en un événement typé (`state["normalized_event"]`) consommé
ensuite par `update_state` (app/graph/nodes/state_update.py). Ce sont les deux SEULS points
d'entrée du graphe (cf. app/graph/build.py, entrée conditionnelle selon
`incoming_event["domain"]`) — aucune autre fonction ne lit `incoming_event` directement.
"""
from __future__ import annotations

import logging
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.state import ConferenceAgentState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]

# Mapping des event_type Control Plane (event-bridge → orchestrateur → forward HTTP, cf.
# doc 03 §4.6) vers un "kind" normalisé — cf. docs/architecture/00-etat-des-lieux.md §2.1 pour
# la liste exhaustive des event_type réellement possibles par cette voie (limitée à 4 côté
# Prosody, enrichie par l'orchestrateur avec les dérivés participant.*).
_CONTROL_KIND_MAP = {
    "muc-room-created": "room_created",
    "room.created": "room_created",
    "muc-room-destroyed": "room_destroyed",
    "room.destroyed": "room_destroyed",
    "muc-occupant-joined": "participant_joined",
    "participant.joined": "participant_joined",
    "muc-occupant-left": "participant_left",
    "participant.left": "participant_left",
}


def build_ingest_control(deps: GraphDeps) -> NodeFunc:
    async def ingest_control_event(state: ConferenceAgentState) -> dict:
        event = state.get("incoming_event") or {}
        event_type = event.get("event_type", "")
        kind = _CONTROL_KIND_MAP.get(event_type)

        if kind is None:
            log.debug(f"[ingest_control_event:{deps.room_id}] type non mappé: {event_type}")
            return {"incoming_event": None, "normalized_event": None}

        return {
            "incoming_event": None,
            "normalized_event": {
                "domain": "control",
                "kind": kind,
                "data": event.get("data", {}),
            },
        }

    return ingest_control_event


# Mapping des événements Data Plane (navigateur headless JITSI_EVENTS_JS, doc 00 §5.5, +
# événements internes du moteur de parole/vision, posés dans app/main.py avant invocation du
# graphe) vers un "kind" normalisé.
_DATA_KIND_MAP = {
    "USER_JOINED": "participant_joined",
    "USER_LEFT": "participant_left",
    "PARTICIPANTS_SNAPSHOT": "participant_snapshot",
    "DISPLAY_NAME_CHANGED": "display_name_changed",
    "USER_ROLE_CHANGED": "role_changed",
    "DOMINANT_SPEAKER_CHANGED": "dominant_speaker_changed",
    "AUDIO_LEVEL": "audio_level",
    "TRACK_MUTE_CHANGED": "track_mute_changed",
    "PARTICIPANT_PROPERTY_CHANGED": "raised_hand_changed",
    "MESSAGE_RECEIVED": "chat_message",
    "PRIVATE_MESSAGE_RECEIVED": "chat_message",
    "REACTION_RECEIVED": "reaction",
    "POLL_RECEIVED": "poll_received",
    "POLL_ANSWER_RECEIVED": "poll_answer_received",
    "SUBJECT_CHANGED": "subject_changed",
    "LOCK_STATE_CHANGED": "lock_state_changed",
    "KICKED": "kicked",
    "PARTICIPANT_KICKED": "participant_kicked",
    "TALK_WHILE_MUTED": "talk_while_muted",
    "NOISY_MIC": "noisy_mic",
    # Événements internes (posés directement par app/main.py, pas par JITSI_EVENTS_JS) :
    "SPEECH_TRANSCRIPT": "speech_transcript",     # GeminiSession.on_transcription
    "AGENT_SPEECH": "agent_speech",                # GeminiSession.on_speech
    "VISION_DESCRIPTION": "vision_description",    # app/perception/vision.py
}

# Événements trop fréquents / sans intérêt pour le raisonnement — mis à jour dans
# SpeakerTracker (via EventBus, cf. app/events/handlers.py) mais volontairement PAS injectés
# dans ConferenceAgentState.conversation pour ne pas noyer le contexte du LLM. Ils alimentent
# quand même `media.current_speaker`/`media.dominant_speaker` via update_state.
_SILENT_KINDS = {"audio_level"}


def build_ingest_data(deps: GraphDeps) -> NodeFunc:
    async def ingest_data_event(state: ConferenceAgentState) -> dict:
        event = state.get("incoming_event") or {}
        event_type = event.get("event_type", "")
        kind = _DATA_KIND_MAP.get(event_type)

        if kind is None:
            log.debug(f"[ingest_data_event:{deps.room_id}] type non mappé: {event_type}")
            return {"incoming_event": None, "normalized_event": None}

        return {
            "incoming_event": None,
            "normalized_event": {
                "domain": "data",
                "kind": kind,
                "silent": kind in _SILENT_KINDS,
                "data": event.get("data", event),
            },
        }

    return ingest_data_event
