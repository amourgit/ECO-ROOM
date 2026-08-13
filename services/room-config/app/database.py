from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from app.models import room_config, room_history  # noqa
    Base.metadata.create_all(bind=engine)


def run_migrations():
    """
    Exécute `alembic upgrade head` programmatiquement au démarrage — pour
    que les colonnes ajoutées aux modèles après la mise en prod initiale
    (ex: peer_enabled/status/source/jitsi_confirmed_at, cf. migrations/versions/
    0001_add_peer_enabled_and_room_status.py) soient TOUJOURS appliquées,
    sans dépendre d'un opérateur qui se souvient de lancer `alembic upgrade
    head` à la main après chaque déploiement.

    `Base.metadata.create_all()` (appelé juste avant, cf. init_db) ne crée
    que les tables manquantes — il ne modifie JAMAIS une table déjà
    existante (limite SQLAlchemy déjà rencontrée sur ce projet, cf.
    PLAN_SYNCHRONISATION_ROOMS_JITSI.md §5 Phase 1). Les migrations Alembic
    sont donc la seule voie fiable pour faire évoluer un schéma déjà en
    production. Toutes les migrations de ce projet sont écrites de façon
    idempotente (IF NOT EXISTS / IF EXISTS) : rejouable sans risque, y
    compris sur une base fraîche où create_all() a déjà tout créé.
    """
    from alembic import command
    from alembic.config import Config

    service_root = Path(__file__).resolve().parent.parent  # .../services/room-config
    alembic_cfg = Config(str(service_root / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(service_root / "migrations"))
    command.upgrade(alembic_cfg, "head")
