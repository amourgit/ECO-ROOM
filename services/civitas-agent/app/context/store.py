"""
ContextStore — PORTÉ DE services/peer/app/context/store.py, sans modification fonctionnelle.

Mémoire niveau 1 ("chaud", RAM) — cf. docs/architecture/01-architecture-cible-civitas-agent.md
§7. Cette classe est instanciée une seule fois par process (donc par room, cf. app/state.py),
ce qui était déjà vrai dans l'ancien peer (un ContextStore par PeerInstance) — le portage ici
est donc purement mécanique, aucune adaptation d'isolation n'était nécessaire sur ce module en
particulier : il n'a jamais eu de logique multi-room.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SpeechEntry:
    speaker_id: str
    speaker_name: str
    text: str
    entry_type: str = "participant"
    timestamp: datetime = field(default_factory=datetime.utcnow)
    # Corrèle l'entrée d'entrée (ce qui a été entendu) et l'entrée de sortie
    # (ce que l'agent a répondu) d'un même tour du moteur de parole.
    turn_id: str | None = None


class ContextStore:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.entries: list[SpeechEntry] = []
        self._started_at = datetime.utcnow()

    def add(self, speaker_id: str, speaker_name: str,
            text: str, entry_type: str = "participant",
            turn_id: str | None = None) -> SpeechEntry:
        e = SpeechEntry(speaker_id, speaker_name, text, entry_type, turn_id=turn_id)
        self.entries.append(e)
        return e

    def seed(self, history_entries: list[dict]) -> int:
        """
        Pré-remplit le store à partir de l'historique persisté (mémoire niveau 2, via
        app/memory/client.py), en tête de liste et en conservant l'ordre chronologique. Utilisé
        au démarrage du process pour retrouver immédiatement toute la mémoire de la réunion,
        même si ce process CIVITAS Agent vient d'être (re)créé (crash-restart de CETTE room
        uniquement, cf. doc 03).
        """
        seeded = []
        for e in history_entries:
            try:
                ts = datetime.fromisoformat(e["occurred_at"])
            except (KeyError, ValueError):
                ts = datetime.utcnow()
            extra = e.get("extra") or {}
            seeded.append(SpeechEntry(
                speaker_id=e.get("speaker_id") or "",
                speaker_name=e.get("speaker_name", "Inconnu"),
                text=e.get("text", ""),
                entry_type=e.get("entry_type", "participant"),
                timestamp=ts,
                turn_id=extra.get("turn_id"),
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
