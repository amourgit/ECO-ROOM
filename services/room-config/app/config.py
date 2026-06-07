from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8010
    API_TOKEN: str = "civitas-room-config-token"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
