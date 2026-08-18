"""
Tests app/registry.py — doc 03 §4.2. Le registre lui-même ne porte aucune garantie
d'isolation (c'est le rôle du process/container par room, doc 03 §3) — il doit seulement être
un mapping fiable room_id → container, jamais mélanger deux entrées.
"""
from app.registry import AgentRegistry, make_handle


def test_put_get_remove():
    r = AgentRegistry()
    h = make_handle("room-a", "civitas-agent-room-a-abc123", "http://civitas-agent-room-a-abc123:8300")
    r.put(h)
    assert r.is_active("room-a")
    assert r.get("room-a")["container_name"] == "civitas-agent-room-a-abc123"
    r.remove("room-a")
    assert not r.is_active("room-a")
    assert r.get("room-a") is None


def test_two_rooms_never_collide():
    r = AgentRegistry()
    r.put(make_handle("room-a", "c-a", "http://c-a:8300"))
    r.put(make_handle("room-b", "c-b", "http://c-b:8300"))
    assert r.get("room-a")["container_name"] == "c-a"
    assert r.get("room-b")["container_name"] == "c-b"
    r.remove("room-a")
    assert r.is_active("room-b")  # retirer une room ne doit jamais affecter les autres


def test_set_status_only_affects_target_room():
    r = AgentRegistry()
    r.put(make_handle("room-a", "c-a", "http://c-a:8300"))
    r.put(make_handle("room-b", "c-b", "http://c-b:8300"))
    r.set_status("room-a", "unhealthy")
    assert r.get("room-a")["status"] == "unhealthy"
    assert r.get("room-b")["status"] == "starting"


def test_list_all_returns_every_active_room():
    r = AgentRegistry()
    r.put(make_handle("room-a", "c-a", "http://c-a:8300"))
    r.put(make_handle("room-b", "c-b", "http://c-b:8300"))
    room_ids = {h["room_id"] for h in r.list_all()}
    assert room_ids == {"room-a", "room-b"}
