from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    JITSI_HOST: str = "meet.civitas.local"
    JITSI_CA_CERT: str = "/certs/civitas.local.crt"
    ROOM_CONFIG_URL: str = "http://civitas-room-config:8010"
    ROOM_CONFIG_TOKEN: str = "civitas-room-config-token"
    KAFKA_BOOTSTRAP: str = "192.168.1.89:9092"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8002
    API_TOKEN: str = "civitas-peer-token"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
