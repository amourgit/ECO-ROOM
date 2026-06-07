import logging
from sqlalchemy.orm import Session
from app.models.room_config import RoomConfig
from app.schemas.room_config import RoomConfigCreate, RoomConfigUpdate, AgentContextResponse
from app.defaults.prompts import DEFAULT_SYSTEM_PROMPT, build_prompt

log = logging.getLogger(__name__)


def get_room_config(db: Session, room_id: str) -> RoomConfig | None:
    return db.query(RoomConfig).filter(RoomConfig.room_id == room_id).first()


def get_or_create_default(db: Session, room_id: str) -> RoomConfig:
    config = get_room_config(db, room_id)
    if config:
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
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    return config


def create_room_config(db: Session, data: RoomConfigCreate) -> RoomConfig:
    existing = get_room_config(db, data.room_id)
    if existing:
        return existing

    prompt = data.system_prompt or build_prompt(
        DEFAULT_SYSTEM_PROMPT,
        agent_name=data.agent_name,
        language=data.language,
        keywords=data.invocation_keywords,
    )
    config = RoomConfig(**data.model_dump(exclude={"system_prompt"}), system_prompt=prompt)
    db.add(config)
    db.commit()
    db.refresh(config)
    log.info(f"[RoomConfig] Config créée: {data.room_id}")
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
        },
        invocation_keywords=config.invocation_keywords,
        tools_allowed=config.tools_allowed,
    )
