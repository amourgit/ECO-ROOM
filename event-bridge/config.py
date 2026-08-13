from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Listener INTERNAL Docker uniquement — jamais l'IP hôte.
    KAFKA_BOOTSTRAP: str = "civitas-kafka:9094"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 8100
    # Secret partagé avec le module Prosody mod_muc_webhook (muc_webhook_secret,
    # cf. jitsi/prosody-plugins-custom/mod_muc_webhook.lua). AVANT : /webhook
    # n'avait AUCUNE authentification — n'importe qui sur le réseau pouvait
    # injecter de faux événements de room/participant dans tout le pipeline
    # CIVITAS (Kafka, room-spawner, spawn de peers...). Cf.
    # PLAN_SYNCHRONISATION_ROOMS_JITSI.md. Valeur par défaut volontairement
    # absurde pour qu'un déploiement qui oublie de la changer soit visible en
    # revue plutôt que silencieusement non sécurisé.
    WEBHOOK_SECRET: str = "CHANGE_ME_MATCH_PROSODY_MUC_WEBHOOK_SECRET"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
