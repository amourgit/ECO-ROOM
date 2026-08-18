"""
Tests app/perception/speaker_tracker.py — porté tel quel (doc 00 §5.2).
"""
import time

from app.perception.speaker_tracker import AUDIO_THRESHOLD, SpeakerTracker


def test_participant_joined_and_left():
    t = SpeakerTracker("room-1")
    t.on_participant_joined("p1", "Alice")
    assert t.count == 1
    assert t.get_name("p1") == "Alice"
    t.on_participant_left("p1")
    assert t.count == 0


def test_dominant_speaker_updates_name_and_current_speaker():
    t = SpeakerTracker("room-1")
    t.on_participant_joined("p1", "Alice")
    t.on_dominant_speaker("p1")
    t.on_track_mute_changed("p1", "audio", False)
    t.on_audio_level("p1", AUDIO_THRESHOLD + 0.1)
    speaker_id, speaker_name = t.current_speaker()
    assert speaker_id == "p1"
    assert speaker_name == "Alice"


def test_muted_participant_is_never_current_speaker():
    t = SpeakerTracker("room-1")
    t.on_participant_joined("p1", "Alice")
    t.on_dominant_speaker("p1")
    t.on_track_mute_changed("p1", "audio", True)  # muet
    t.on_audio_level("p1", AUDIO_THRESHOLD + 0.5)
    speaker_id, _ = t.current_speaker()
    assert speaker_id is None


def test_snapshot_reconstructs_participants():
    t = SpeakerTracker("room-1")
    t.on_snapshot([
        {"id": "p1", "name": "Alice", "role": "moderator", "isMuted": False,
         "isVideoMuted": True, "raisedHand": False},
        {"id": "p2", "name": "Bob", "role": "participant", "isMuted": True,
         "isVideoMuted": True, "raisedHand": True},
    ])
    assert t.count == 2
    assert t.participants["p1"].role == "moderator"
    assert t.participants["p2"].raised_hand is True


def test_snapshot_dict_shape_consumed_by_state_update():
    """cf. app/graph/nodes/state_update.py — le format de snapshot() doit rester stable."""
    t = SpeakerTracker("room-1")
    t.on_participant_joined("p1", "Alice")
    snap = t.snapshot()
    assert "room_participants" in snap
    assert "dominant_speaker" in snap
    assert "current_speaker" in snap
    assert snap["total_participants"] == 1


def test_left_participant_clears_dominant_speaker():
    t = SpeakerTracker("room-1")
    t.on_participant_joined("p1", "Alice")
    t.on_dominant_speaker("p1")
    t.on_participant_left("p1")
    _, name = t.current_speaker()
    assert name == "Participant"
