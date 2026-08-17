"""
ConferenceAgentState — l'état unifié consolidant Control Plane et Data Plane pour UNE room.

Cf. docs/architecture/01-architecture-cible-civitas-agent.md §5.

Invariant fondamental (garantie d'isolation, doc 03 §2) :
    conference.room_id est fixé une seule fois, à la création de l'état initial, depuis
    Settings.ROOM_ID (app/config.py) — aucune fonction de ce module ni d'ailleurs dans le
    graphe ne le réassigne jamais. Il n'existe donc, par construction, aucun état atteignable
    qui référence une autre room que celle du process.
"""
from __future__ import annotations

import operator
from datetime import datetime, timezone
from typing import Annotated, Literal, TypedDict

BehaviorMode = Literal["on_call", "proactive", "silent"]
ResponseMode = Literal["audio", "text", "none"]
AgentStatus = Literal["starting", "active", "silent", "stopping", "stopped"]
EntryType = Literal["participant", "agent", "chat"]


class ParticipantState(TypedDict):
    endpoint_id: str
    display_name: str
    role: str                      # "moderator" | "participant"
    is_muted: bool
    is_video_muted: bool
    raised_hand: bool
    audio_level: float
    joined_at: str                 # ISO8601


class ConversationEntry(TypedDict):
    speaker_id: str | None
    speaker_name: str
    text: str
    entry_type: EntryType
    turn_id: str | None
    timestamp: str                 # ISO8601


class MediaState(TypedDict):
    dominant_speaker_id: str | None
    dominant_speaker_name: str
    current_speaker_id: str | None
    current_speaker_name: str
    last_screen_description: str | None
    recording_active: bool


class ConferenceMeta(TypedDict):
    room_id: str                   # cf. invariant en tête de fichier — jamais réassigné
    subject: str | None
    locked: bool
    lobby_enabled: bool
    av_moderation_enabled: bool
    started_at: str                # ISO8601


class AgentAction(TypedDict):
    tool: str                      # nom qualifié, ex: "moderation_tools.kick_participant"
    args: dict
    reason: str                    # justification produite par le nœud `reason`
    requested_at: str              # ISO8601


def _merge_participants(
    left: dict[str, ParticipantState], right: dict[str, ParticipantState]
) -> dict[str, ParticipantState]:
    """Réducteur LangGraph : fusion par endpoint_id, la mise à jour la plus récente gagne."""
    merged = dict(left)
    merged.update(right)
    return merged


class ConferenceAgentState(TypedDict):
    """
    État complet consommé/produit par chaque nœud du graphe (cf. doc 01 §6). Les champs
    `Annotated[..., operator.add]` utilisent le mécanisme de réduction natif de LangGraph pour
    accumuler plutôt qu'écraser (conversation, pending_actions) — les autres champs sont
    remplacés intégralement à chaque mise à jour (fusion faite explicitement dans le nœud
    `state_update`, cf. app/graph/nodes/state_update.py).
    """

    conference: ConferenceMeta
    participants: dict[str, ParticipantState]
    conversation: Annotated[list[ConversationEntry], operator.add]
    media: MediaState
    current_topic: str | None
    agenda: list[str]
    pending_actions: Annotated[list[AgentAction], operator.add]
    response_mode: ResponseMode
    agent_status: AgentStatus

    # Champ TRANSITOIRE : l'événement brut en cours de traitement par CETTE invocation du
    # graphe (cf. app/graph/nodes/ingest.py). Posé par l'appelant (app/main.py) à chaque
    # `graph.ainvoke(...)`, consommé et remis à None par `ingest_control_event`/
    # `ingest_data_event` avant que le reste du graphe ne s'exécute — jamais lu après ce
    # point. Il fait partie du schéma d'état (donc du checkpoint) uniquement parce que
    # LangGraph exige un schéma d'état unique pour tous les nœuds ; sa valeur persistée entre
    # deux invocations n'a aucune signification et est toujours écrasée avant lecture.
    incoming_event: dict | None

    # Champs TRANSITOIRES supplémentaires, même statut que incoming_event ci-dessus — jamais
    # significatifs d'une invocation du graphe à l'autre.
    normalized_event: dict | None   # produit par ingest_control_event/ingest_data_event
    route_decision: str | None      # "respond" | "tool_only" | "ignore" — produit par `route`
    actions_to_execute: list[AgentAction]  # produit par `reason`, consommé et vidé par `act`
                                            # (overwrite à chaque invocation — contrairement à
                                            # `pending_actions` ci-dessus qui est un JOURNAL
                                            # cumulatif de tout ce qui a été exécuté, conservé
                                            # pour l'observabilité et la persistance, doc 01 §6)


def initial_state(room_id: str) -> ConferenceAgentState:
    """
    Construit l'état initial pour CETTE room. Appelé une seule fois, au démarrage du process
    (app/main.py), avec Settings.ROOM_ID — jamais rappelé avec un autre room_id pendant la vie
    du process (cf. invariant en tête de fichier).
    """
    now = datetime.now(timezone.utc).isoformat()
    return ConferenceAgentState(
        conference=ConferenceMeta(
            room_id=room_id,
            subject=None,
            locked=False,
            lobby_enabled=False,
            av_moderation_enabled=False,
            started_at=now,
        ),
        participants={},
        conversation=[],
        media=MediaState(
            dominant_speaker_id=None,
            dominant_speaker_name="Participant",
            current_speaker_id=None,
            current_speaker_name="Participant",
            last_screen_description=None,
            recording_active=False,
        ),
        current_topic=None,
        agenda=[],
        pending_actions=[],
        response_mode="audio",
        agent_status="starting",
        incoming_event=None,
        normalized_event=None,
        route_decision=None,
        actions_to_execute=[],
    )
