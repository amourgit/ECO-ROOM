from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8010
    API_TOKEN: str = "civitas-room-config-token"

    # Consumer d'historique — écoute room.transcriptions pour persister
    # durablement toutes les interactions de réunion.
    # Listener INTERNAL Docker uniquement — jamais l'IP hôte.
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"
    HISTORY_KAFKA_ENABLED: bool = True

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
