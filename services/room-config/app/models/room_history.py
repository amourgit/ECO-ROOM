from datetime import datetime
from sqlalchemy import String, Text, DateTime, JSON, BigInteger, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class RoomHistoryEntry(Base):
    """
    Historique complet et persistant des interactions d'une réunion :
    paroles des participants (transcrites), paroles de l'agent, messages chat.

    C'est la source de vérité durable — alimentée en continu par le consumer
    Kafka (topic `room.transcriptions`), donc totalement découplée du cycle
    de vie du service `peer`. Un crash/redémarrage du peer, ou même une
    reconnexion Gemini, ne fait jamais perdre cet historique : il vit ici,
    pas dans la RAM d'un process agent.
    """
    __tablename__ = "room_history_entries"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    room_id: Mapped[str] = mapped_column(String(255), nullable=False)
    speaker_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    speaker_name: Mapped[str] = mapped_column(String(255), nullable=False)
    # participant | agent | chat
    entry_type: Mapped[str] = mapped_column(String(32), nullable=False, default="participant")
    text: Mapped[str] = mapped_column(Text, nullable=False)
    # Champ libre : snapshot room, endpoint_id, etc. — extensible sans migration.
    extra: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    occurred_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index("ix_room_history_room_occurred", "room_id", "occurred_at"),
    )
