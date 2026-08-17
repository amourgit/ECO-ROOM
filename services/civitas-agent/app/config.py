"""
Configuration du CIVITAS Agent.

Différence fondamentale avec services/peer/app/config.py : ROOM_ID est ici un champ
OBLIGATOIRE, sans valeur par défaut. C'est la garantie structurelle d'isolation par room
(cf. docs/architecture/03-isolation-et-orchestration.md §2) — un process qui ne reçoit pas de
ROOM_ID au démarrage doit échouer immédiatement (pydantic-settings lève une ValidationError),
jamais démarrer "en mode dégradé multi-room" comme le faisait l'ancien PeerManager.
"""
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── Identité de la room — LA garantie d'isolation (cf. doc 03 §2) ──────────────────────
    ROOM_ID: str

    # ── Gemini Live (moteur de parole par défaut, cf. app/speech/engine.py) ────────────────
    GEMINI_API_KEY: str

    # ── Jitsi (porte n°2, navigateur headless — cf. doc 00 §2.2) ───────────────────────────
    JITSI_HOST: str = "meet.civitas.local"
    JITSI_CA_CERT: str = "/certs/civitas.local.crt"

    # ── CIVITAS Platform — room-config (mémoire niveau 2 + config, cf. doc 01 §7) ──────────
    ROOM_CONFIG_URL: str = "http://civitas-room-config:8010"
    ROOM_CONFIG_TOKEN: str = "civitas-room-config-token"

    # ── Kafka — listener INTERNAL Docker uniquement, jamais l'IP hôte ──────────────────────
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"

    # ── Checkpoint LangGraph (doc 01 §7, niveau 3) — thread_id = ROOM_ID, toujours ──────────
    CHECKPOINT_DATABASE_URL: str = (
        "postgresql://civitas:civitas2024@civitas-postgres:5432/room_config"
    )

    # ── Mémoire de réunion (identique à l'ancien peer) ──────────────────────────────────────
    HISTORY_REHYDRATE_LIMIT: int = 300
    CONTEXT_MAX_ENTRIES: int = 80
    ORAL_REQUEST_KEYWORDS: str = "oral,voix,parle,vocal,dis à voix,à voix haute,audio"

    # ── API de contrôle locale (adressée uniquement par civitas-orchestrator, doc 03 §4.3) ─
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8300
    API_TOKEN: str = "civitas-agent-token"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
