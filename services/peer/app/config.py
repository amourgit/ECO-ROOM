from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    JITSI_HOST: str = "meet.civitas.local"
    JITSI_CA_CERT: str = "/certs/civitas.local.crt"
    ROOM_CONFIG_URL: str = "http://civitas-room-config:8010"
    ROOM_CONFIG_TOKEN: str = "civitas-room-config-token"
    # Communication inter-conteneurs Docker -> listener INTERNAL (jamais l'IP hôte).
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8002
    API_TOKEN: str = "civitas-peer-token"

    # Mémoire de réunion : nombre d'entrées rapatriées depuis l'historique
    # persisté (room-config/Postgres) au (re)join, et nombre d'entrées
    # réinjectées dans Gemini à chaque (re)connexion de la session Live.
    HISTORY_REHYDRATE_LIMIT: int = 300
    CONTEXT_MAX_ENTRIES: int = 80

    # Mots-clés (séparés par des virgules) qui, dans un message chat,
    # demandent explicitement une réponse orale plutôt qu'écrite.
    # cf. app/peer/response_policy.py
    ORAL_REQUEST_KEYWORDS: str = "oral,voix,parle,vocal,dis à voix,à voix haute,audio"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
