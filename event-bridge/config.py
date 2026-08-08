from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Listener INTERNAL Docker uniquement — jamais l'IP hôte.
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8100

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
