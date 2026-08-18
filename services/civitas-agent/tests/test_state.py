"""
Tests app/state.py — cf. docs/architecture/01-architecture-cible-civitas-agent.md §5.
"""
from app.state import initial_state


def test_initial_state_room_id_matches_argument():
    state = initial_state("ma-room-42")
    assert state["conference"]["room_id"] == "ma-room-42"


def test_initial_state_is_empty_and_starting():
    state = initial_state("r1")
    assert state["participants"] == {}
    assert state["conversation"] == []
    assert state["pending_actions"] == []
    assert state["agent_status"] == "starting"
    assert state["response_mode"] == "audio"


def test_initial_state_transient_fields_are_none_or_empty():
    """Les champs transitoires (doc 01 §6) ne doivent jamais porter de valeur significative
    avant la première invocation du graphe."""
    state = initial_state("r1")
    assert state["incoming_event"] is None
    assert state["normalized_event"] is None
    assert state["route_decision"] is None
    assert state["actions_to_execute"] == []


def test_two_rooms_never_share_mutable_state():
    """Garantie d'isolation (doc 03 §2) au niveau le plus élémentaire : deux appels à
    initial_state() pour deux rooms différentes ne doivent jamais partager le même objet
    mutable sous-jacent (participants, conversation, etc.)."""
    a = initial_state("room-a")
    b = initial_state("room-b")
    a["participants"]["ghost"] = {"endpoint_id": "ghost"}
    assert "ghost" not in b["participants"], (
        "Fuite inter-room détectée : les deux états partagent le même dict participants"
    )
