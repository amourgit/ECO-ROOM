from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP: str = "192.168.1.89:9092"
    PEER_SERVICE_URL: str = "http://civitas-peer:8002"
    ROOM_CONFIG_URL: str = "http://civitas-room-config:8010"
    ROOM_CONFIG_TOKEN: str = "civitas-room-config-token"
    PEER_SERVICE_TOKEN: str = "civitas-peer-token"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8011
    AUTO_JOIN: bool = True
    AUTO_LEAVE: bool = True

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
