"""
Tests des routes `/moderator/*` (app/main.py) — valide la parité fidèle avec l'ancien
`services/room-spawner/app/spawner.py` (vérifiée ligne par ligne avant réécriture, cf.
docs/architecture/04-plan-migration.md) et corrige deux bugs réels découverts pendant cette
vérification :

  1. `moderator_standby` appelait à tort `agent_client.shutdown()` (détruit le container) —
     l'original `set_peer_standby` ne fait qu'un PATCH `behavior_mode=silent`, sans jamais
     couper l'agent (standby = figurant silencieux, pas éjection).
  2. `moderator_activate` aliasait à tort sur `moderator_inject` (spawn un nouveau container)
     — l'original `activate_peer` ne fait qu'un PATCH `behavior_mode=on_call` sur un agent
     déjà actif, sans jamais en spawner un nouveau.

Ces tests appellent les fonctions de route directement (pas de TestClient HTTP complet) : le
lifespan de l'app (app.main::lifespan) tente de se connecter à Kafka et à Docker au démarrage,
tous deux indisponibles dans cet environnement de test (cf.
docs/architecture/04-plan-migration.md — nécessite l'environnement de déploiement réel) — les
gestionnaires de route eux-mêmes sont de simples fonctions async, testables isolément en
mockant les dépendances qu'ils appellent.
"""
from unittest.mock import AsyncMock, patch

import pytest

from app import main
from app.registry import make_handle


@pytest.fixture(autouse=True)
def clean_registry():
    """Chaque test repart d'un registre vide — évite toute fuite d'état entre tests."""
    main.registry._entries.clear()
    yield
    main.registry._entries.clear()


@pytest.mark.asyncio
async def test_inject_persists_agent_enabled_before_spawn_when_not_active():
    with patch("app.main.set_agent_enabled", new=AsyncMock(return_value=True)) as set_enabled, \
         patch.object(main.runtime_provider, "spawn", new=AsyncMock(
             return_value=make_handle("salle-1", "civitas-agent-salle-1", "http://civitas-agent-salle-1:8300")
         )) as spawn:
        result = await main.moderator_inject(room_id="salle-1", _=None)

    set_enabled.assert_awaited_once_with("salle-1", True)
    spawn.assert_awaited_once()
    assert result["status"] == "injected"
    assert main.registry.is_active("salle-1")


@pytest.mark.asyncio
async def test_inject_still_persists_agent_enabled_even_if_already_active():
    """Même comportement que l'original inject_peer : la persistance a lieu même si un agent
    tourne déjà — seul le spawn est court-circuité."""
    main.registry.put(make_handle("salle-1", "civitas-agent-salle-1", "http://x:8300"))

    with patch("app.main.set_agent_enabled", new=AsyncMock(return_value=True)) as set_enabled, \
         patch.object(main.runtime_provider, "spawn", new=AsyncMock()) as spawn:
        result = await main.moderator_inject(room_id="salle-1", _=None)

    set_enabled.assert_awaited_once_with("salle-1", True)
    spawn.assert_not_called()
    assert result["already_active"] is True


@pytest.mark.asyncio
async def test_eject_persists_agent_enabled_false_before_teardown():
    main.registry.put(make_handle("salle-1", "civitas-agent-salle-1", "http://x:8300"))

    with patch("app.main.set_agent_enabled", new=AsyncMock(return_value=True)) as set_enabled, \
         patch.object(main.runtime_provider, "teardown", new=AsyncMock()) as teardown:
        result = await main.moderator_eject(room_id="salle-1", _=None)

    set_enabled.assert_awaited_once_with("salle-1", False)
    teardown.assert_awaited_once()
    assert result["status"] == "ejected"
    assert not main.registry.is_active("salle-1")


@pytest.mark.asyncio
async def test_eject_persists_flag_even_when_no_agent_currently_active():
    with patch("app.main.set_agent_enabled", new=AsyncMock(return_value=True)) as set_enabled, \
         patch.object(main.runtime_provider, "teardown", new=AsyncMock()) as teardown:
        result = await main.moderator_eject(room_id="salle-vide", _=None)

    set_enabled.assert_awaited_once_with("salle-vide", False)
    teardown.assert_not_called()
    assert result["status"] == "not_active"


@pytest.mark.asyncio
async def test_standby_never_tears_down_the_container():
    """Régression du bug corrigé : standby NE DOIT JAMAIS appeler teardown/shutdown."""
    main.registry.put(make_handle("salle-1", "civitas-agent-salle-1", "http://x:8300"))

    with patch("app.main.set_behavior_mode", new=AsyncMock(return_value=True)) as set_mode, \
         patch.object(main.runtime_provider, "teardown", new=AsyncMock()) as teardown, \
         patch.object(main.agent_client, "shutdown", new=AsyncMock()) as agent_shutdown, \
         patch.object(main.agent_client, "reload_config", new=AsyncMock()) as reload_cfg:
        result = await main.moderator_standby(room_id="salle-1", _=None)

    set_mode.assert_awaited_once_with("salle-1", "silent")
    teardown.assert_not_called()
    agent_shutdown.assert_not_called()
    reload_cfg.assert_awaited_once()  # amélioration délibérée : rechargement en direct
    assert main.registry.is_active("salle-1")  # le container est TOUJOURS là
    assert result["status"] == "standby"
    assert result["live_reload"] is True


@pytest.mark.asyncio
async def test_standby_on_inactive_room_still_persists_but_skips_live_reload():
    with patch("app.main.set_behavior_mode", new=AsyncMock(return_value=True)) as set_mode, \
         patch.object(main.agent_client, "reload_config", new=AsyncMock()) as reload_cfg:
        result = await main.moderator_standby(room_id="salle-jamais-active", _=None)

    set_mode.assert_awaited_once_with("salle-jamais-active", "silent")
    reload_cfg.assert_not_called()
    assert result["live_reload"] is False


@pytest.mark.asyncio
async def test_activate_never_spawns_a_new_container():
    """Régression du bug corrigé : activate NE DOIT JAMAIS appeler spawn (contrairement à
    l'ancienne implémentation qui aliasait à tort sur moderator_inject)."""
    main.registry.put(make_handle("salle-1", "civitas-agent-salle-1", "http://x:8300"))

    with patch("app.main.set_behavior_mode", new=AsyncMock(return_value=True)) as set_mode, \
         patch.object(main.runtime_provider, "spawn", new=AsyncMock()) as spawn, \
         patch("app.main.set_agent_enabled", new=AsyncMock()) as set_enabled, \
         patch.object(main.agent_client, "reload_config", new=AsyncMock()) as reload_cfg:
        result = await main.moderator_activate(room_id="salle-1", _=None)

    set_mode.assert_awaited_once_with("salle-1", "on_call")
    spawn.assert_not_called()
    set_enabled.assert_not_called()  # activate ne touche jamais agent_enabled, seulement behavior_mode
    reload_cfg.assert_awaited_once()
    assert result["status"] == "active"


@pytest.mark.asyncio
async def test_standby_then_activate_round_trip_calls_are_symmetric():
    main.registry.put(make_handle("salle-1", "civitas-agent-salle-1", "http://x:8300"))

    with patch("app.main.set_behavior_mode", new=AsyncMock(return_value=True)) as set_mode, \
         patch.object(main.agent_client, "reload_config", new=AsyncMock()):
        await main.moderator_standby(room_id="salle-1", _=None)
        await main.moderator_activate(room_id="salle-1", _=None)

    assert set_mode.await_args_list[0].args == ("salle-1", "silent")
    assert set_mode.await_args_list[1].args == ("salle-1", "on_call")
