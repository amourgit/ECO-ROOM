import logging
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.room_config import RoomConfig
from app.schemas.room_config import (
    RoomConfigCreate, RoomConfigUpdate, RoomReserveRequest, AgentContextResponse,
)
from app.defaults.prompts import DEFAULT_SYSTEM_PROMPT, build_prompt

log = logging.getLogger(__name__)


def get_room_config(db: Session, room_id: str) -> RoomConfig | None:
    return db.query(RoomConfig).filter(RoomConfig.room_id == room_id).first()


def get_or_create_default(db: Session, room_id: str) -> RoomConfig:
    """
    Endpoint appelé par le peer au (re)join — cf. GET /rooms/{room_id}/context.

    C'est le point de confirmation le plus fiable qu'une room Jitsi est
    réellement en train d'être utilisée : room-spawner n'appelle ce chemin
    (via is_peer_enabled -> get_room_context) qu'en réaction à un véritable
    événement Prosody muc-room-created reçu par Kafka — jamais de façon
    spéculative. cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §3-4.

    - Aucune config existante -> room ad-hoc (jamais réservée à l'avance) :
      créée directement "confirmed", source="jitsi_event".
    - Config existante en "pending" (réservée via POST /rooms/reserve, room
      Jitsi pas encore vue) -> promue "confirmed" ici, preuve réelle reçue.
    - Config existante déjà "confirmed" -> inchangée (no-op idempotent).
    """
    config = get_room_config(db, room_id)
    if config:
        if config.status == "pending":
            config.status = "confirmed"
            config.jitsi_confirmed_at = datetime.utcnow()
            db.commit()
            db.refresh(config)
            log.info(f"[RoomConfig] Room confirmée (réservation -> réelle): {room_id}")
        return config

    log.info(f"[RoomConfig] Création config par défaut pour room: {room_id}")
    prompt = build_prompt(
        DEFAULT_SYSTEM_PROMPT,
        agent_name="CIVITAS",
        language="fr",
        keywords=["civitas"],
    )
    config = RoomConfig(
        room_id=room_id,
        agent_name="CIVITAS",
        system_prompt=prompt,
        status="confirmed",
        source="jitsi_event",
        jitsi_confirmed_at=datetime.utcnow(),
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    return config


def create_room_config(db: Session, data: RoomConfigCreate) -> RoomConfig:
    """
    Création directe legacy (POST /rooms/) — AUCUNE vérification qu'une room
    Jitsi réelle correspond à ce room_id. Conservée telle quelle pour
    rétrocompatibilité (cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §5 Phase 1),
    mais désormais tracée explicitement : source="manager_api_legacy",
    status="confirmed" (jamais vérifié, "confirmed" ici par convention
    historique, pas par preuve réelle). Préférer POST /rooms/reserve pour
    tout nouvel usage.
    """
    existing = get_room_config(db, data.room_id)
    if existing:
        return existing

    prompt = data.system_prompt or build_prompt(
        DEFAULT_SYSTEM_PROMPT,
        agent_name=data.agent_name,
        language=data.language,
        keywords=data.invocation_keywords,
    )
    config = RoomConfig(
        **data.model_dump(exclude={"system_prompt"}),
        system_prompt=prompt,
        status="confirmed",
        source="manager_api_legacy",
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    log.info(f"[RoomConfig] Config créée (legacy, non vérifiée): {data.room_id}")
    return config


def reserve_room_config(db: Session, data: RoomReserveRequest) -> RoomConfig:
    """
    POST /rooms/reserve — flux correct Cas A (cf. §3-4 du plan). Réserve les
    métadonnées CIVITAS AVANT que la room Jitsi réelle existe, statut
    "pending" jusqu'à preuve réelle (cf. get_or_create_default). Idempotent :
    si le room_id existe déjà, retourne la ligne existante sans la modifier.
    """
    existing = get_room_config(db, data.room_id)
    if existing:
        return existing

    prompt = data.system_prompt or build_prompt(
        DEFAULT_SYSTEM_PROMPT,
        agent_name=data.agent_name,
        language=data.language,
        keywords=data.invocation_keywords,
    )
    config = RoomConfig(
        **data.model_dump(exclude={"system_prompt"}),
        system_prompt=prompt,
        status="pending",
        source="manager_api_reserved",
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    log.info(f"[RoomConfig] Room réservée (pending): {data.room_id}")
    return config


def update_room_config(db: Session, room_id: str, data: RoomConfigUpdate) -> RoomConfig | None:
    config = get_room_config(db, room_id)
    if not config:
        return None
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(config, field, value)
    db.commit()
    db.refresh(config)
    log.info(f"[RoomConfig] Config mise à jour: {room_id}")
    return config


def delete_room_config(db: Session, room_id: str) -> bool:
    config = get_room_config(db, room_id)
    if not config:
        return False
    db.delete(config)
    db.commit()
    return True


def list_room_configs(db: Session, skip: int = 0, limit: int = 100) -> list[RoomConfig]:
    return db.query(RoomConfig).offset(skip).limit(limit).all()


def build_agent_context(config: RoomConfig) -> AgentContextResponse:
    return AgentContextResponse(
        room_id=config.room_id,
        agent_name=config.agent_name,
        system_prompt=config.system_prompt,
        behavior_mode=config.behavior_mode,
        language=config.language,
        permissions={
            "can_speak": config.can_speak,
            "can_write_chat": config.can_write_chat,
            "can_use_tools": config.can_use_tools,
            "can_use_rag": config.can_use_rag,
            "can_moderate": config.can_moderate,
            # Corrige le bug §2.3/§7.5 du plan : is_peer_enabled() (room-spawner)
            # lisait déjà ce chemin (permissions.peer_enabled) mais la clé
            # n'existait jamais ici -> retombait systématiquement sur son
            # défaut True, quoi qu'un modérateur ait fait via /moderator/eject.
            "peer_enabled": config.peer_enabled,
        },
        invocation_keywords=config.invocation_keywords,
        tools_allowed=config.tools_allowed,
    )
