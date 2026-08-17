from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"

    ROOM_CONFIG_URL: str = "http://civitas-room-config:8010"
    ROOM_CONFIG_TOKEN: str = "civitas-room-config-token"

    # Spawn dynamique — cf. docs/architecture/03-isolation-et-orchestration.md §4.3
    AGENT_IMAGE: str = "civitas-agent-runtime:latest"
    AGENT_NETWORK: str = "civitas-net"
    AGENT_INTERNAL_PORT: int = 8300
    AGENT_SHM_SIZE: str = "2g"
    AGENT_MEM_LIMIT: str = "1g"
    AGENT_API_TOKEN: str = "civitas-agent-token"

    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8011
    MODERATOR_API_TOKEN: str = "civitas-moderator-token"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
