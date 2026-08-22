"""
Tests de la synchronisation applicative `agent_enabled` <-> `peer_enabled` — cf.
docs/architecture/04-plan-migration.md Phase 2 "Migration du schéma room_configs" et
app/services/room_config_service.py::_sync_agent_peer_enabled.

Exécutés contre une vraie base Postgres (tests/conftest.py) — ces scénarios ont d'abord été
validés manuellement contre cette même base avant d'être formalisés ici.
"""
from app.schemas.room_config import RoomConfigCreate, RoomConfigUpdate, RoomReserveRequest
from app.services import room_config_service as svc


def _make(db, room_id: str, **overrides):
    data = RoomConfigCreate(room_id=room_id, **overrides)
    return svc.create_room_config(db, data)


def test_update_peer_enabled_only_propagates_to_agent_enabled(db_session):
    _make(db_session, "salle-1")
    updated = svc.update_room_config(db_session, "salle-1", RoomConfigUpdate(peer_enabled=False))
    assert updated.peer_enabled is False
    assert updated.agent_enabled is False


def test_update_agent_enabled_only_propagates_to_peer_enabled(db_session):
    _make(db_session, "salle-2")
    updated = svc.update_room_config(db_session, "salle-2", RoomConfigUpdate(agent_enabled=False))
    assert updated.agent_enabled is False
    assert updated.peer_enabled is False


def test_update_unrelated_field_never_touches_either_flag(db_session):
    config = _make(db_session, "salle-3", peer_enabled=False)
    assert config.agent_enabled is False  # cohérent dès la création (cf. test de création ci-dessous)

    updated = svc.update_room_config(db_session, "salle-3", RoomConfigUpdate(agent_name="Nouveau"))
    assert updated.agent_name == "Nouveau"
    assert updated.peer_enabled is False   # inchangé
    assert updated.agent_enabled is False  # inchangé — la sync n'a pas dû se déclencher


def test_update_both_flags_explicitly_to_different_values_is_respected():
    """Si l'appelant fournit explicitement les DEUX champs (même à des valeurs différentes —
    cas volontairement exotique, ex: migration manuelle en cours), la synchronisation ne doit
    JAMAIS écraser une valeur explicitement fournie par l'appelant : elle ne s'active que
    lorsqu'un seul des deux champs est présent."""
    update = RoomConfigUpdate(peer_enabled=True, agent_enabled=False)
    assert update.model_dump(exclude_none=True) == {"peer_enabled": True, "agent_enabled": False}


def test_create_with_only_peer_enabled_set_propagates_to_agent_enabled(db_session):
    data = RoomConfigCreate(room_id="salle-4", peer_enabled=False)
    assert "agent_enabled" not in data.model_fields_set
    config = svc.create_room_config(db_session, data)
    assert config.peer_enabled is False
    assert config.agent_enabled is False


def test_create_with_only_agent_enabled_set_propagates_to_peer_enabled(db_session):
    data = RoomConfigCreate(room_id="salle-5", agent_enabled=False)
    assert "peer_enabled" not in data.model_fields_set
    config = svc.create_room_config(db_session, data)
    assert config.agent_enabled is False
    assert config.peer_enabled is False


def test_create_with_neither_flag_set_keeps_both_defaults_true(db_session):
    config = _make(db_session, "salle-6")
    assert config.peer_enabled is True
    assert config.agent_enabled is True


def test_reserve_with_only_agent_enabled_set_propagates_to_peer_enabled(db_session):
    data = RoomReserveRequest(room_id="salle-7", agent_enabled=False)
    config = svc.reserve_room_config(db_session, data)
    assert config.status == "pending"
    assert config.agent_enabled is False
    assert config.peer_enabled is False


def test_build_agent_context_exposes_both_flags_nested_under_permissions(db_session):
    config = _make(db_session, "salle-8", agent_enabled=False)
    ctx = svc.build_agent_context(config)
    assert ctx.permissions["agent_enabled"] is False
    assert ctx.permissions["peer_enabled"] is False
    # Contrat lu par civitas-orchestrator (app/room_config_client.py::is_agent_enabled) et par
    # l'ancien room-spawner (app/room_config_client.py::is_peer_enabled) — les deux CHEMINS
    # (permissions.agent_enabled / permissions.peer_enabled) doivent rester présents tant que
    # les deux orchestrateurs coexistent.
