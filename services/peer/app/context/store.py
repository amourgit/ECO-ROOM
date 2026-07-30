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

    def seed(self, history_entries: list[dict]) -> int:
        """
        Pré-remplit le store à partir de l'historique persisté (room-config),
        en tête de liste et en conservant l'ordre chronologique. Utilisé au
        (re)join pour retrouver immédiatement toute la mémoire de la réunion,
        même si cette instance de PeerInstance vient d'être (re)créée.
        """
        seeded = []
        for e in history_entries:
            try:
                ts = datetime.fromisoformat(e["occurred_at"])
            except (KeyError, ValueError):
                ts = datetime.utcnow()
            seeded.append(SpeechEntry(
                speaker_id=e.get("speaker_id") or "",
                speaker_name=e.get("speaker_name", "Inconnu"),
                text=e.get("text", ""),
                entry_type=e.get("entry_type", "participant"),
                timestamp=ts,
            ))
        self.entries = seeded + self.entries
        return len(seeded)

    def build_context(self, max_entries: int = 50) -> str:
        recent = self.entries[-max_entries:]
        return "\n".join(
            f"[{e.timestamp.strftime('%H:%M:%S')}] {e.speaker_name}: {e.text}"
            for e in recent
        )

    @property
    def is_empty(self) -> bool:
        return not self.entries

    def duration_minutes(self) -> int:
        return int((datetime.utcnow() - self._started_at).total_seconds() / 60)
