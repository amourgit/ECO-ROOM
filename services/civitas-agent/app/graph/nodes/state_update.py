"""
update_state — doc 01 §6. Fusionne `state["normalized_event"]` (produit par
app/graph/nodes/ingest.py) dans ConferenceAgentState. Seul nœud du graphe qui écrit dans
`participants`/`conversation`/`media`/`conference` — toute la logique de fusion vit ici, pas
éparpillée dans les nœuds d'ingestion (qui ne font QUE normaliser, jamais fusionner).
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.state import ConferenceAgentState, ParticipantState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_participant(participants: dict, pid: str, name: str = "Inconnu") -> ParticipantState:
    return participants.get(pid) or ParticipantState(
        endpoint_id=pid, display_name=name, role="participant",
        is_muted=False, is_video_muted=True, raised_hand=False,
        audio_level=0.0, joined_at=_now(),
    )


def build_update_state(deps: GraphDeps) -> NodeFunc:
    async def update_state(state: ConferenceAgentState) -> dict:
        norm = state.get("normalized_event")
        if not norm:
            return {}

        kind = norm["kind"]
        data = norm.get("data", {})
        participants = dict(state["participants"])
        media = dict(state["media"])
        conference = dict(state["conference"])
        conversation_additions: list[dict] = []

        pid = data.get("participantId") or data.get("endpoint_id")
        name = data.get("name") or data.get("display_name") or "Inconnu"

        if kind == "room_created":
            conference["started_at"] = _now()

        elif kind == "room_destroyed":
            pass  # le process s'arrête via app/main.py, rien à faire côté state

        elif kind == "participant_snapshot":
            for p in data.get("participants", []):
                eid = p.get("id")
                if not eid:
                    continue
                participants[eid] = ParticipantState(
                    endpoint_id=eid, display_name=p.get("name", "Inconnu"),
                    role=p.get("role", "participant"), is_muted=p.get("isMuted", False),
                    is_video_muted=p.get("isVideoMuted", True),
                    raised_hand=p.get("raisedHand", False),
                    audio_level=0.0, joined_at=_now(),
                )

        elif kind == "participant_joined" and pid:
            participants[pid] = _ensure_participant(participants, pid, name)
            participants[pid]["display_name"] = name
            participants[pid]["role"] = data.get("role", "participant")

        elif kind == "participant_left" and pid:
            participants.pop(pid, None)
            if media.get("dominant_speaker_id") == pid:
                media["dominant_speaker_id"] = None
                media["dominant_speaker_name"] = "Participant"

        elif kind == "display_name_changed" and pid:
            p = _ensure_participant(participants, pid, name)
            p["display_name"] = name
            participants[pid] = p

        elif kind == "role_changed" and pid:
            p = _ensure_participant(participants, pid, name)
            p["role"] = data.get("role", "participant")
            participants[pid] = p

        elif kind == "dominant_speaker_changed":
            media["dominant_speaker_id"] = pid
            media["dominant_speaker_name"] = name
            media["current_speaker_id"] = pid
            media["current_speaker_name"] = name

        elif kind == "audio_level" and pid:
            if pid in participants:
                participants[pid]["audio_level"] = data.get("level", 0.0)

        elif kind == "track_mute_changed" and pid:
            p = _ensure_participant(participants, pid, name)
            if data.get("type") == "audio":
                p["is_muted"] = bool(data.get("muted"))
            elif data.get("type") == "video":
                p["is_video_muted"] = bool(data.get("muted"))
            participants[pid] = p

        elif kind == "raised_hand_changed" and pid:
            if data.get("property") == "raisedHand":
                p = _ensure_participant(participants, pid, name)
                p["raised_hand"] = bool(data.get("raisedHand"))
                participants[pid] = p

        elif kind == "chat_message":
            conversation_additions.append({
                "speaker_id": pid, "speaker_name": name,
                "text": data.get("text", ""), "entry_type": "chat",
                "turn_id": None, "timestamp": _now(),
            })

        elif kind == "speech_transcript":
            conversation_additions.append({
                "speaker_id": media.get("current_speaker_id"),
                "speaker_name": media.get("current_speaker_name", "Participant"),
                "text": data.get("text", ""), "entry_type": "participant",
                "turn_id": data.get("turn_id"), "timestamp": _now(),
            })

        elif kind == "agent_speech":
            conversation_additions.append({
                "speaker_id": None, "speaker_name": deps.room_config.get("agent_name", "CIVITAS"),
                "text": data.get("text", ""), "entry_type": "agent",
                "turn_id": data.get("turn_id"), "timestamp": _now(),
            })

        elif kind == "vision_description":
            media["last_screen_description"] = data.get("description")

        elif kind == "subject_changed":
            conference["subject"] = data.get("subject")

        elif kind == "lock_state_changed":
            conference["locked"] = bool(data.get("locked"))

        elif kind in ("kicked", "participant_kicked", "reaction", "poll_received",
                      "poll_answer_received", "talk_while_muted", "noisy_mic"):
            # Capturés (doc 00 §5.5 / doc 02 §10) mais sans effet structurel sur l'état
            # au-delà de ce que le nœud `route`/`reason` en fera directement à partir de
            # `normalized_event` — pas de mutation de participants/media nécessaire ici.
            pass

        else:
            log.debug(f"[update_state:{deps.room_id}] kind non géré: {kind}")

        update: dict = {
            "participants": participants,
            "media": media,
            "conference": conference,
        }
        if conversation_additions:
            update["conversation"] = conversation_additions  # réduit via operator.add (state.py)
        return update

    return update_state
