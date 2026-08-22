"""
conftest.py — suite de tests de `room-config` contre une VRAIE base Postgres dédiée
(`room_config_test`, distincte de la base de développement/production), pas une simulation
SQLite. Justification : la logique testée ici (migrations Alembic, colonnes `BOOLEAN NOT NULL
DEFAULT`, synchronisation `agent_enabled`/`peer_enabled`) est directement dépendante du
dialecte Postgres réellement utilisé en production (`DATABASE_URL`, cf. `.env.example`) — une
base SQLite in-memory aurait pu masquer des différences de comportement SQL, en particulier
sur `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`, syntaxe spécifique à Postgres.

Deux fixtures :
  - `pg_engine` (session, ne change jamais après le premier test) : recrée le schéma depuis
    zéro (`alembic upgrade head`) une seule fois pour toute la session de tests.
  - `db_session` (function) : une session par test, encapsulée dans une transaction annulée
    (`rollback()`) à la fin de CHAQUE test — aucun test ne peut donc polluer l'état vu par le
    suivant, sans avoir à recréer le schéma à chaque fois (coût prohibitif pour une suite qui
    grandira).
"""
import os

os.environ.setdefault(
    "DATABASE_URL", "postgresql://civitas:civitas2024@127.0.0.1:5432/room_config_test"
)
os.environ.setdefault("HISTORY_KAFKA_ENABLED", "false")

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="session")
def pg_engine():
    from pathlib import Path

    from alembic import command
    from alembic.config import Config

    from app.config import get_settings
    from app.database import Base

    settings = get_settings()
    engine = create_engine(settings.DATABASE_URL)

    # Schéma toujours reconstruit à zéro en début de session de tests — jamais d'état résiduel
    # d'une exécution précédente qui pourrait fausser un test (ex: colonne déjà migrée alors
    # que le test veut précisément valider la migration qui l'ajoute).
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS room_configs CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS room_history_entries CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE"))

    # Reproduit EXACTEMENT la séquence de démarrage réelle (app/main.py::lifespan) :
    # init_db() [Base.metadata.create_all(), crée les tables via les modèles SQLAlchemy
    # ACTUELS] PUIS run_migrations() [alembic upgrade head, no-op ici puisque create_all() a
    # déjà tout créé — cf. docstring de 0001/0002, IF NOT EXISTS]. Sans ce create_all()
    # préalable, `alembic upgrade head` échoue dès 0001 : ses `ALTER TABLE room_configs ADD
    # COLUMN` supposent que la table existe déjà (elle n'est jamais créée par les migrations
    # elles-mêmes, seulement modifiée — cf. commentaire déjà présent dans app/database.py).
    from app.models import room_config, room_history  # noqa: F401 — enregistre les modèles
    Base.metadata.create_all(bind=engine)

    service_root = Path(__file__).resolve().parent.parent
    alembic_cfg = Config(str(service_root / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(service_root / "migrations"))
    alembic_cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
    command.upgrade(alembic_cfg, "head")

    yield engine
    engine.dispose()


@pytest.fixture()
def db_session(pg_engine):
    connection = pg_engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connection)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
