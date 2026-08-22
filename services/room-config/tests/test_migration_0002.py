"""
Test dédié de la migration `0002_add_agent_enabled` — simule une base EXISTANTE réelle
(schéma d'avant ce changement, lignes avec des valeurs `peer_enabled` hétérogènes) puis
applique la migration et vérifie le backfill ligne par ligne. Complète
tests/test_agent_enabled_sync.py, qui teste la couche service sur un schéma déjà à jour.

Important : le schéma "avant migration" est construit ici via SQL BRUT, PAS via
`Base.metadata.create_all()` — celui-ci utiliserait les modèles SQLAlchemy ACTUELS, qui
incluent déjà `agent_enabled` (cf. app/models/room_config.py), ce qui rendrait ce test
incapable de reproduire un déploiement réellement antérieur à cette migration. C'est
exactement le même principe que la validation manuelle faite avant l'écriture de ce fichier
(schéma créé avant modification du code, cf. commit associé).

Utilise sa PROPRE base Postgres dédiée (créée/détruite dans ce module), indépendante de
`room_config_test` (tests/conftest.py), pour contrôler précisément l'état du schéma sans
entrer en conflit avec les autres tests.
"""
from pathlib import Path

import pytest
from sqlalchemy import create_engine, text

TEST_DB_NAME = "room_config_test_migration"
ADMIN_URL = "postgresql://civitas:civitas2024@127.0.0.1:5432/postgres"
TEST_DB_URL = f"postgresql://civitas:civitas2024@127.0.0.1:5432/{TEST_DB_NAME}"

# Schéma EXACT produit par la migration 0001 (donc avant agent_enabled) — cf.
# migrations/versions/0001_add_peer_enabled_and_room_status.py pour la liste de colonnes de
# référence. Toute évolution de 0001 doit être reportée ici pour que ce test reste fidèle.
PRE_0002_SCHEMA_SQL = """
CREATE TABLE room_configs (
    room_id VARCHAR(255) PRIMARY KEY,
    agent_name VARCHAR(100) NOT NULL DEFAULT 'CIVITAS',
    system_prompt TEXT NOT NULL DEFAULT '',
    behavior_mode VARCHAR(50) NOT NULL DEFAULT 'on_call',
    language VARCHAR(10) NOT NULL DEFAULT 'fr',
    can_speak BOOLEAN NOT NULL DEFAULT TRUE,
    can_write_chat BOOLEAN NOT NULL DEFAULT TRUE,
    can_use_tools BOOLEAN NOT NULL DEFAULT FALSE,
    can_use_rag BOOLEAN NOT NULL DEFAULT FALSE,
    can_moderate BOOLEAN NOT NULL DEFAULT FALSE,
    peer_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    invocation_keywords JSON NOT NULL DEFAULT '["civitas"]',
    tools_allowed JSON NOT NULL DEFAULT '[]',
    extra_config JSON NOT NULL DEFAULT '{}',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    status VARCHAR(20) NOT NULL DEFAULT 'confirmed',
    source VARCHAR(50) NOT NULL DEFAULT 'manager_api_legacy',
    jitsi_confirmed_at TIMESTAMP NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
)
"""


def _alembic_config(db_url: str):
    from alembic.config import Config

    service_root = Path(__file__).resolve().parent.parent
    cfg = Config(str(service_root / "alembic.ini"))
    cfg.set_main_option("script_location", str(service_root / "migrations"))
    cfg.set_main_option("sqlalchemy.url", db_url)
    return cfg


@pytest.fixture()
def migration_db():
    """
    Function-scoped (pas session/module) : chaque test repart d'une base neuve, aucune
    dépendance à l'ordre d'exécution des tests de ce fichier.

    Point d'attention important : migrations/env.py lit délibérément
    `get_settings().DATABASE_URL` à chaque invocation d'une commande Alembic (jamais l'URL
    passée via `Config.set_main_option`, qui n'est qu'une valeur de repli côté script offline
    — cf. commentaire explicite dans migrations/env.py, "jamais dupliquée en dur... pour ne
    jamais risquer une désynchronisation avec ce que l'application utilise réellement"). Or
    `get_settings()` est `@lru_cache` (app/config.py) : une fois appelé une première fois
    ailleurs dans la session de tests (ex: tests/conftest.py::pg_engine), il reste figé sur
    CETTE valeur pour tout le reste du process, même après modification de `os.environ`. Sans
    `cache_clear()` explicite ici, les commandes Alembic de ce module s'exécuteraient donc en
    silence contre `room_config_test` (la base des AUTRES tests) plutôt que contre
    `room_config_test_migration` — bug réel rencontré et corrigé pendant l'écriture de ce test
    (cf. commit associé), pas une précaution théorique.
    """
    import os

    from app.config import get_settings

    admin_engine = create_engine(ADMIN_URL, isolation_level="AUTOCOMMIT")
    with admin_engine.connect() as conn:
        conn.execute(text(f'DROP DATABASE IF EXISTS "{TEST_DB_NAME}"'))
        conn.execute(text(f'CREATE DATABASE "{TEST_DB_NAME}" OWNER civitas'))
    admin_engine.dispose()

    previous_url = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = TEST_DB_URL
    get_settings.cache_clear()

    yield TEST_DB_URL

    if previous_url is not None:
        os.environ["DATABASE_URL"] = previous_url
    else:
        os.environ.pop("DATABASE_URL", None)
    get_settings.cache_clear()

    admin_engine = create_engine(ADMIN_URL, isolation_level="AUTOCOMMIT")
    with admin_engine.connect() as conn:
        conn.execute(text(f'DROP DATABASE IF EXISTS "{TEST_DB_NAME}"'))
    admin_engine.dispose()


def test_migration_0002_backfills_per_row_and_is_fully_reversible(migration_db):
    from alembic import command

    engine = create_engine(migration_db)

    # 1. Construit le schéma PRÉ-migration via SQL brut (pas Base.metadata.create_all(), cf.
    #    docstring de module) et informe Alembic que cette base en est déjà à la révision 0001
    #    (command.stamp — pose la marque de version sans rejouer 0001, puisque le schéma
    #    construit ci-dessus EST déjà exactement le résultat de 0001).
    with engine.begin() as conn:
        conn.execute(text(PRE_0002_SCHEMA_SQL))
    command.stamp(_alembic_config(migration_db), "0001")

    with engine.begin() as conn:
        cols = {r[0] for r in conn.execute(text(
            "SELECT column_name FROM information_schema.columns WHERE table_name='room_configs'"
        ))}
    assert "agent_enabled" not in cols, "précondition violée : agent_enabled ne doit pas encore exister"
    assert "peer_enabled" in cols

    # 2. Insère des lignes avec des valeurs peer_enabled HÉTÉROGÈNES — reproduit une base
    #    réelle avec un historique d'éjections manuelles (cf. tests/test_agent_enabled_sync.py).
    rows = [("room-a", True), ("room-b", False), ("room-c", True), ("room-d", False)]
    with engine.begin() as conn:
        for room_id, peer_enabled in rows:
            conn.execute(text(
                "INSERT INTO room_configs (room_id, peer_enabled) VALUES (:room_id, :peer_enabled)"
            ), {"room_id": room_id, "peer_enabled": peer_enabled})

    # 3. Applique la migration cible et vérifie le backfill EXACT, ligne par ligne.
    command.upgrade(_alembic_config(migration_db), "0002")

    with engine.begin() as conn:
        result = conn.execute(text(
            "SELECT room_id, peer_enabled, agent_enabled FROM room_configs ORDER BY room_id"
        )).fetchall()
    actual = {r[0]: (r[1], r[2]) for r in result}
    for room_id, expected in rows:
        peer_enabled, agent_enabled = actual[room_id]
        assert peer_enabled == expected, f"{room_id}: peer_enabled inattendu"
        assert agent_enabled == expected, (
            f"{room_id}: backfill incorrect — agent_enabled={agent_enabled} "
            f"attendu={expected} (doit reproduire peer_enabled)"
        )

    # 4. Réversibilité complète : downgrade retire la colonne sans toucher au reste, et un
    #    nouvel upgrade la restaure proprement (pas de résidu ni d'erreur de rejeu).
    command.downgrade(_alembic_config(migration_db), "0001")
    with engine.begin() as conn:
        cols_after_downgrade = {r[0] for r in conn.execute(text(
            "SELECT column_name FROM information_schema.columns WHERE table_name='room_configs'"
        ))}
    assert "agent_enabled" not in cols_after_downgrade
    assert "peer_enabled" in cols_after_downgrade

    command.upgrade(_alembic_config(migration_db), "0002")
    with engine.begin() as conn:
        cols_after_reupgrade = {r[0] for r in conn.execute(text(
            "SELECT column_name FROM information_schema.columns WHERE table_name='room_configs'"
        ))}
    assert "agent_enabled" in cols_after_reupgrade

    engine.dispose()
