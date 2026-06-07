from datetime import datetime
from sqlalchemy import String, Text, Boolean, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class RoomConfig(Base):
    __tablename__ = "room_configs"

    room_id: Mapped[str] = mapped_column(String(255), primary_key=True, index=True)
    agent_name: Mapped[str] = mapped_column(String(100), default="CIVITAS")
    system_prompt: Mapped[str] = mapped_column(Text)
    behavior_mode: Mapped[str] = mapped_column(String(50), default="on_call")
    language: Mapped[str] = mapped_column(String(10), default="fr")
    can_speak: Mapped[bool] = mapped_column(Boolean, default=True)
    can_write_chat: Mapped[bool] = mapped_column(Boolean, default=True)
    can_use_tools: Mapped[bool] = mapped_column(Boolean, default=False)
    can_use_rag: Mapped[bool] = mapped_column(Boolean, default=False)
    can_moderate: Mapped[bool] = mapped_column(Boolean, default=False)
    invocation_keywords: Mapped[list] = mapped_column(JSON, default=lambda: ["civitas"])
    tools_allowed: Mapped[list] = mapped_column(JSON, default=list)
    extra_config: Mapped[dict] = mapped_column(JSON, default=dict)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
