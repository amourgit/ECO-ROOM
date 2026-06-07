from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SpeechEntry:
    speaker_id: str
    speaker_name: str
    text: str
    entry_type: str = "participant"
    timestamp: datetime = field(default_factory=datetime.utcnow)


class ContextStore:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.entries: list[SpeechEntry] = []
        self._started_at = datetime.utcnow()

    def add(self, speaker_id: str, speaker_name: str,
            text: str, entry_type: str = "participant") -> SpeechEntry:
        e = SpeechEntry(speaker_id, speaker_name, text, entry_type)
        self.entries.append(e)
        return e

    def build_context(self, max_entries: int = 50) -> str:
        recent = self.entries[-max_entries:]
        return "\n".join(
            f"[{e.timestamp.strftime('%H:%M:%S')}] {e.speaker_name}: {e.text}"
            for e in recent
        )

    def duration_minutes(self) -> int:
        return int((datetime.utcnow() - self._started_at).total_seconds() / 60)
