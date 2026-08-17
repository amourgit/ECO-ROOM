"""
Handlers d'événements Jitsi — PORTÉS DE services/peer/app/events/handlers.py, sans
modification fonctionnelle. Un handler par domaine, composés via EventBus.register()
(cf. app/events/bus.py).
"""
import logging
from typing import Callable

log = logging.getLogger(__name__)


def make_speaker_handler(tracker) -> Callable:
    """Met à jour le SpeakerTracker (app/perception/speaker_tracker.py) à chaque événement
    participant/audio. Doit être le PREMIER handler enregistré (les autres en dépendent)."""
    async def handler(event_type: str, data: dict):
        if event_type == "PARTICIPANTS_SNAPSHOT":
            tracker.on_snapshot(data.get("participants", []))

        elif event_type == "USER_JOINED":
            tracker.on_participant_joined(
                data["participantId"],
                data.get("name", "Inconnu"),
                data.get("role", "participant"),
            )

        elif event_type == "USER_LEFT":
            tracker.on_participant_left(data["participantId"])

        elif event_type == "DISPLAY_NAME_CHANGED":
            tracker.on_display_name_changed(data["participantId"], data.get("name", ""))

        elif event_type == "USER_ROLE_CHANGED":
            tracker.on_role_changed(data["participantId"], data.get("role", "participant"))

        elif event_type == "DOMINANT_SPEAKER_CHANGED":
            tracker.on_dominant_speaker(data["participantId"])

        elif event_type == "AUDIO_LEVEL":
            tracker.on_audio_level(data["participantId"], data.get("level", 0.0))

        elif event_type == "TRACK_MUTE_CHANGED":
            tracker.on_track_mute_changed(
                data["participantId"],
                data.get("type", "audio"),
                data.get("muted", True),
            )

        elif event_type == "PARTICIPANT_PROPERTY_CHANGED":
            if data.get("property") == "raisedHand":
                tracker.on_raised_hand(
                    data["participantId"],
                    data.get("raisedHand", False),
                )

    return handler


def make_log_handler(room_id: str) -> Callable:
    """Log structuré de tous les événements (hors AUDIO_LEVEL trop fréquent)."""
    async def handler(event_type: str, data: dict):
        if event_type == "AUDIO_LEVEL":
            return

        icons = {
            "USER_JOINED": "👤+", "USER_LEFT": "👤-", "USER_ROLE_CHANGED": "🔑",
            "DISPLAY_NAME_CHANGED": "✏️", "DOMINANT_SPEAKER_CHANGED": "🎙️",
            "TALK_WHILE_MUTED": "🔇", "NOISY_MIC": "📢", "TRACK_MUTE_CHANGED": "🔊",
            "MESSAGE_RECEIVED": "💬", "PRIVATE_MESSAGE_RECEIVED": "🔒💬",
            "REACTION_RECEIVED": "😊", "PARTICIPANT_PROPERTY_CHANGED": "⚙️",
            "POLL_RECEIVED": "📊", "POLL_ANSWER_RECEIVED": "📊✓",
            "SUBJECT_CHANGED": "📝", "LOCK_STATE_CHANGED": "🔒",
            "KICKED": "❌", "PARTICIPANT_KICKED": "❌", "PARTICIPANTS_SNAPSHOT": "📸",
        }
        icon = icons.get(event_type, "📡")

        if event_type in ("USER_JOINED", "USER_LEFT"):
            log.info(f"[Event:{room_id}] {icon} {event_type} — {data.get('name')} ({data.get('participantId')})")
        elif event_type == "DOMINANT_SPEAKER_CHANGED":
            log.info(f"[Event:{room_id}] {icon} {data.get('name')} ({data.get('participantId')})")
        elif event_type == "TRACK_MUTE_CHANGED":
            action = "mute" if data.get("muted") else "unmute"
            log.info(f"[Event:{room_id}] {icon} {data.get('name')} {action} {data.get('type')}")
        elif event_type == "MESSAGE_RECEIVED":
            log.info(f"[Event:{room_id}] {icon} [{data.get('name')}]: {str(data.get('text',''))[:80]}")
        elif event_type == "PARTICIPANT_PROPERTY_CHANGED":
            if data.get("property") == "raisedHand":
                action = "✋ lève" if data.get("raisedHand") else "👇 baisse"
                log.info(f"[Event:{room_id}] {action} la main — {data.get('name')}")
        elif event_type == "PARTICIPANTS_SNAPSHOT":
            names = [p.get("name") for p in data.get("participants", [])]
            log.info(f"[Event:{room_id}] {icon} Snapshot: {names}")
        else:
            log.info(f"[Event:{room_id}] {icon} {event_type}: {data}")

    return handler


def make_kafka_handler(room_id: str, kafka) -> Callable:
    """Publie les événements pertinents sur Kafka (topics inchangés, doc 00 §7)."""
    async def handler(event_type: str, data: dict):
        if event_type in ("AUDIO_LEVEL", "DOMINANT_SPEAKER_CHANGED"):
            return

        if event_type in ("USER_JOINED", "USER_LEFT"):
            await kafka.publish_participant_event(room_id, f"participant.{'joined' if event_type == 'USER_JOINED' else 'left'}", {
                "participantId": data.get("participantId"),
                "name": data.get("name"),
                "role": data.get("role"),
                "totalParticipants": len(data.get("participants", [])),
            })

        elif event_type == "USER_ROLE_CHANGED":
            await kafka.publish_participant_event(room_id, "participant.role_changed", {
                "participantId": data.get("participantId"),
                "name": data.get("name"),
                "role": data.get("role"),
            })

        elif event_type == "TRACK_MUTE_CHANGED":
            await kafka.publish_participant_event(room_id, "participant.mute_changed", {
                "participantId": data.get("participantId"),
                "name": data.get("name"),
                "type": data.get("type"),
                "muted": data.get("muted"),
            })

        elif event_type == "PARTICIPANT_PROPERTY_CHANGED":
            if data.get("property") == "raisedHand":
                evt = "participant.hand_raised" if data.get("raisedHand") else "participant.hand_lowered"
                await kafka.publish_participant_event(room_id, evt, {
                    "participantId": data.get("participantId"),
                    "name": data.get("name"),
                })

        elif event_type == "REACTION_RECEIVED":
            await kafka.publish_participant_event(room_id, "participant.reaction", {
                "participantId": data.get("participantId"),
                "name": data.get("name"),
                "reaction": data.get("reaction"),
            })

        elif event_type in ("POLL_RECEIVED", "POLL_ANSWER_RECEIVED"):
            evt = "poll.received" if event_type == "POLL_RECEIVED" else "poll.answer"
            await kafka.publish_participant_event(room_id, evt, data)

        elif event_type == "SUBJECT_CHANGED":
            await kafka.publish_room_event(room_id, "room.subject_changed", {"subject": data.get("subject")})

        elif event_type in ("KICKED", "PARTICIPANT_KICKED"):
            await kafka.publish_participant_event(room_id, "participant.kicked", data)

    return handler


def make_moderation_handler(room_id: str, browser, context: dict) -> Callable:
    """Réactions de modération automatique (levé de main, parle muté, etc.) — inchangé."""
    async def handler(event_type: str, data: dict):
        if context.get("behavior_mode") == "silent":
            return

        if event_type == "TALK_WHILE_MUTED":
            name = data.get("name", "Participant")
            await browser.send_chat(f"💡 {name}, votre micro est coupé — nous ne vous entendons pas.")

        elif event_type == "PARTICIPANT_PROPERTY_CHANGED":
            if data.get("raisedHand"):
                name = data.get("name", "Participant")
                await browser.send_chat(f"✋ {name} a levé la main.")

    return handler
