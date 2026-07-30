from datetime import datetime
from sqlalchemy.orm import Session
from app.models.room_history import RoomHistoryEntry

MAX_LIMIT = 1000
DEFAULT_LIMIT = 200


def add_entry(
    db: Session,
    room_id: str,
    speaker_name: str,
    text: str,
    entry_type: str = "participant",
    speaker_id: str | None = None,
    extra: dict | None = None,
    occurred_at: datetime | None = None,
) -> RoomHistoryEntry:
    entry = RoomHistoryEntry(
        room_id=room_id,
        speaker_id=speaker_id,
        speaker_name=speaker_name,
        entry_type=entry_type,
        text=text,
        extra=extra,
        occurred_at=occurred_at or datetime.utcnow(),
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_history(db: Session, room_id: str, limit: int = DEFAULT_LIMIT) -> list[RoomHistoryEntry]:
    """Retourne les `limit` dernières entrées, en ordre chronologique croissant."""
    limit = max(1, min(limit, MAX_LIMIT))
    rows = (
        db.query(RoomHistoryEntry)
        .filter(RoomHistoryEntry.room_id == room_id)
        .order_by(RoomHistoryEntry.occurred_at.desc())
        .limit(limit)
        .all()
    )
    return list(reversed(rows))


def format_context(entries: list[RoomHistoryEntry]) -> str:
    return "\n".join(
        f"[{e.occurred_at.strftime('%H:%M:%S')}] {e.speaker_name}: {e.text}"
        for e in entries
    )
