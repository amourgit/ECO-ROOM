"""
Configuration du CIVITAS Agent.

Différence fondamentale avec services/peer/app/config.py : ROOM_ID est ici un champ
OBLIGATOIRE, sans valeur par défaut. C'est la garantie structurelle d'isolation par room
(cf. docs/architecture/03-isolation-et-orchestration.md §2) — un process qui ne reçoit pas de
ROOM_ID au démarrage doit échouer immédiatement (pydantic-settings lève une ValidationError),
jamais démarrer "en mode dégradé multi-room" comme le faisait l'ancien PeerManager.

Deuxième différence, ajoutée après remarque explicite : le modèle utilisé n'est plus figé sur
Gemini. Les variables `SPEECH_MODEL_*`/`REASONING_MODEL_*` ci-dessous permettent de choisir et
paramétrer le fournisseur de modèle indépendamment du code — cf.
docs/architecture/05-gestionnaire-de-modeles.md pour l'architecture complète du gestionnaire de
modèles neutre (app/models/).
"""
import json
import logging
from functools import lru_cache

from pydantic import model_validator
from pydantic_settings import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    # ── Identité de la room — LA garantie d'isolation (cf. doc 03 §2) ──────────────────────
    ROOM_ID: str

    # ── Moteur de parole (Data Plane, temps réel) — NEUTRE, cf. doc 05 ──────────────────────
    # Fournisseurs supportés nativement : "gemini_live" (défaut) | "openai_realtime".
    # D'autres fournisseurs peuvent être ajoutés sans toucher au reste du CIVITAS Agent —
    # cf. app/models/speech/factory.py.
    SPEECH_MODEL_PROVIDER: str = "gemini_live"
    SPEECH_MODEL_NAME: str = "gemini-2.5-flash-native-audio-preview-12-2025"
    SPEECH_MODEL_API_KEY: str = ""
    SPEECH_MODEL_VOICE: str = "Aoede"
    SPEECH_MODEL_LANGUAGE: str = "fr"
    # Échappatoire pour tout paramètre propre à un fournisseur qui ne mérite pas sa propre
    # variable d'environnement dédiée (JSON libre) — cf. doc 05 §3.
    SPEECH_MODEL_EXTRA: str = "{}"

    # ── Modèle de raisonnement (sélection d'outils, doc 01 §6 nœud `reason`) — NEUTRE ──────
    # Vide par défaut = raisonnement heuristique conservé (comportement historique, doc 00
    # §5.6) ; renseigner ces variables active le raisonnement outillé réel — cf. doc 05 §4.
    # Fournisseurs supportés : "gemini" | "openai" | "anthropic".
    REASONING_MODEL_PROVIDER: str = ""
    REASONING_MODEL_NAME: str = ""
    REASONING_MODEL_API_KEY: str = ""
    REASONING_MODEL_EXTRA: str = "{}"

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

    @model_validator(mode="after")
    def _backward_compat_gemini_api_key(self) -> "Settings":
        """
        Compatibilité ascendante : les déploiements existants (et `.env` déjà en place)
        positionnent `GEMINI_API_KEY`, pas encore `SPEECH_MODEL_API_KEY`. `extra="ignore"`
        fait que pydantic-settings lit silencieusement `GEMINI_API_KEY` sans le rejeter, mais
        sans non plus le rattacher à `SPEECH_MODEL_API_KEY` automatiquement — on le fait ici
        explicitement, uniquement en repli (`SPEECH_MODEL_API_KEY` déjà renseigné prime
        toujours). Documenté plutôt que silencieux : un avertissement est loggé la première
        fois que ce repli est utilisé.
        """
        import os

        if not self.SPEECH_MODEL_API_KEY:
            legacy = os.environ.get("GEMINI_API_KEY", "")
            if legacy:
                log.warning(
                    "[Settings] GEMINI_API_KEY est déprécié — utiliser SPEECH_MODEL_API_KEY "
                    "(cf. docs/architecture/05-gestionnaire-de-modeles.md). Valeur reprise "
                    "en repli pour cette fois."
                )
                object.__setattr__(self, "SPEECH_MODEL_API_KEY", legacy)
        return self

    def speech_model_extra(self) -> dict:
        """Parse SPEECH_MODEL_EXTRA en dict, dégradation gracieuse sur JSON invalide (jamais
        une exception qui empêcherait le démarrage pour un simple paramètre optionnel)."""
        try:
            return json.loads(self.SPEECH_MODEL_EXTRA) if self.SPEECH_MODEL_EXTRA else {}
        except json.JSONDecodeError:
            log.warning("[Settings] SPEECH_MODEL_EXTRA invalide (JSON) — ignoré")
            return {}

    def reasoning_model_extra(self) -> dict:
        try:
            return json.loads(self.REASONING_MODEL_EXTRA) if self.REASONING_MODEL_EXTRA else {}
        except json.JSONDecodeError:
            log.warning("[Settings] REASONING_MODEL_EXTRA invalide (JSON) — ignoré")
            return {}


@lru_cache
def get_settings() -> Settings:
    return Settings()
