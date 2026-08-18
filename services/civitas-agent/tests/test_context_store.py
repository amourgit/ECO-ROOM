"""
Tests app/context/store.py — mémoire niveau 1 (doc 01 §7), portée telle quelle.
"""
from app.context.store import ContextStore


def test_add_and_build_context():
    store = ContextStore("room-1")
    store.add("p1", "Alice", "Bonjour tout le monde")
    store.add("p2", "Bob", "Salut Alice")
    ctx = store.build_context()
    assert "Alice: Bonjour tout le monde" in ctx
    assert "Bob: Salut Alice" in ctx


def test_is_empty():
    store = ContextStore("room-1")
    assert store.is_empty
    store.add("p1", "Alice", "Un message")
    assert not store.is_empty


def test_seed_prepends_history_in_chronological_order():
    store = ContextStore("room-1")
    store.add("p1", "Alice", "Message live 1")
    seeded = store.seed([
        {"speaker_id": "p0", "speaker_name": "Historique", "text": "Ancien message",
         "entry_type": "participant", "occurred_at": "2025-01-01T10:00:00", "extra": {}},
    ])
    assert seeded == 1
    assert store.entries[0].text == "Ancien message"
    assert store.entries[1].text == "Message live 1"


def test_seed_handles_missing_or_invalid_occurred_at_gracefully():
    store = ContextStore("room-1")
    seeded = store.seed([
        {"speaker_id": "p0", "speaker_name": "X", "text": "sans date", "extra": {}},
    ])
    assert seeded == 1  # ne doit jamais lever d'exception, cf. dégradation gracieuse (doc 00 §5.3)


def test_build_context_respects_max_entries():
    store = ContextStore("room-1")
    for i in range(10):
        store.add("p1", "Alice", f"Message {i}")
    ctx = store.build_context(max_entries=3)
    assert "Message 9" in ctx
    assert "Message 0" not in ctx
