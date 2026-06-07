"""
SpeakerTracker — identification du locuteur actif en temps réel.

Basé sur le document Jitsi :
  - DOMINANT_SPEAKER_CHANGED : signal certifié JVB (RFC6464 audio level dans RTP)
    C'est la méthode officielle — le JVB agrège les niveaux audio de chaque
    endpoint et émet DominantSpeakerEndpointChangeEvent.
  - TRACK_AUDIO_LEVEL_CHANGED : niveau par track (0-1), complément local.

Mapping garanti :
  endpoint_id (= participantId dans lib-jitsi-meet) ↔ display_name
  Ce mapping est maintenu via USER_JOINED / DISPLAY_NAME_CHANGED.
"""
import time
import logging
from dataclasses import dataclass, field
from typing import Optional

log = logging.getLogger(__name__)

AUDIO_THRESHOLD   = 0.04   # niveau minimal pour considérer qu'un participant parle
AUDIO_WINDOW_SEC  = 2.0    # fenêtre glissante pour les niveaux audio


@dataclass
class ParticipantInfo:
    endpoint_id:  str
    display_name: str
    role:         str  = "participant"
    is_muted:     bool = False
    is_video_muted: bool = True
    raised_hand:  bool = False
    audio_level:  float = 0.0
    audio_ts:     float = field(default_factory=time.monotonic)


class SpeakerTracker:
    """
    Maintient l'état en temps réel de tous les participants
    et identifie le locuteur actif.

    Interface LangGraph-ready :
      - snapshot()  → dict complet consommable par un agent
      - current_speaker() → (endpoint_id, display_name)
    """

    def __init__(self, room_id: str):
        self.room_id = room_id
        self._participants: dict[str, ParticipantInfo] = {}
        self._dominant_id:   Optional[str] = None
        self._dominant_name: str           = "Participant"

    # ── Mise à jour depuis les événements Jitsi ───────────────────────────────

    def on_participant_joined(self, endpoint_id: str, display_name: str, role: str = "participant"):
        self._participants[endpoint_id] = ParticipantInfo(
            endpoint_id=endpoint_id,
            display_name=display_name,
            role=role,
        )
        log.info(f"[SpeakerTracker:{self.room_id}] +participant {display_name} ({endpoint_id})")

    def on_participant_left(self, endpoint_id: str):
        p = self._participants.pop(endpoint_id, None)
        if p:
            log.info(f"[SpeakerTracker:{self.room_id}] -participant {p.display_name} ({endpoint_id})")
        if self._dominant_id == endpoint_id:
            self._dominant_id   = None
            self._dominant_name = "Participant"

    def on_display_name_changed(self, endpoint_id: str, display_name: str):
        if endpoint_id in self._participants:
            self._participants[endpoint_id].display_name = display_name
        if self._dominant_id == endpoint_id:
            self._dominant_name = display_name

    def on_role_changed(self, endpoint_id: str, role: str):
        if endpoint_id in self._participants:
            self._participants[endpoint_id].role = role

    def on_dominant_speaker(self, endpoint_id: str):
        """
        Signal JVB certifié — le plus fiable.
        Correspond à DominantSpeakerEndpointChangeEvent du JVB.
        """
        self._dominant_id = endpoint_id
        if endpoint_id in self._participants:
            self._dominant_name = self._participants[endpoint_id].display_name
        log.info(
            f"[SpeakerTracker:{self.room_id}] 🎙️ Dominant: "
            f"{self._dominant_name} ({endpoint_id})"
        )

    def on_audio_level(self, endpoint_id: str, level: float):
        """Niveau audio par track — complément local au dominant speaker JVB."""
        if endpoint_id in self._participants:
            p = self._participants[endpoint_id]
            p.audio_level = level
            p.audio_ts    = time.monotonic()

    def on_track_mute_changed(self, endpoint_id: str, track_type: str, muted: bool):
        if endpoint_id in self._participants:
            p = self._participants[endpoint_id]
            if track_type == "audio":
                p.is_muted = muted
            elif track_type == "video":
                p.is_video_muted = muted

    def on_raised_hand(self, endpoint_id: str, raised: bool):
        if endpoint_id in self._participants:
            self._participants[endpoint_id].raised_hand = raised

    def on_snapshot(self, participants: list[dict]):
        """Snapshot initial au démarrage — participants déjà présents."""
        for p in participants:
            eid = p.get("id")
            if eid:
                self._participants[eid] = ParticipantInfo(
                    endpoint_id=eid,
                    display_name=p.get("name", "Inconnu"),
                    role=p.get("role", "participant"),
                    is_muted=p.get("isMuted", False),
                    is_video_muted=p.get("isVideoMuted", True),
                    raised_hand=p.get("raisedHand", False),
                )
        log.info(
            f"[SpeakerTracker:{self.room_id}] Snapshot: "
            f"{len(self._participants)} participants — "
            f"{[p.display_name for p in self._participants.values()]}"
        )

    # ── Résolution du locuteur ────────────────────────────────────────────────

    def current_speaker(self) -> tuple[Optional[str], str]:
        """
        Retourne (endpoint_id, display_name) du locuteur actuel.

        Priorité :
          1. DOMINANT_SPEAKER si son niveau audio est récent et non muté
          2. Participant avec le niveau audio le plus élevé dans la fenêtre
          3. (None, "Participant") si silence / ambigu
        """
        now = time.monotonic()

        # Participants actifs (audio récent et non muted)
        active = {
            eid: p for eid, p in self._participants.items()
            if (not p.is_muted
                and p.audio_level >= AUDIO_THRESHOLD
                and now - p.audio_ts < AUDIO_WINDOW_SEC)
        }

        if not active:
            # Fallback : dominant speaker même sans niveau audio récent
            if self._dominant_id and self._dominant_id in self._participants:
                p = self._participants[self._dominant_id]
                if not p.is_muted:
                    return (self._dominant_id, p.display_name)
            return (None, "Participant")

        # Dominant speaker si actif → priorité absolue (signal JVB certifié)
        if self._dominant_id and self._dominant_id in active:
            return (self._dominant_id, active[self._dominant_id].display_name)

        # Sinon : participant avec le niveau le plus élevé
        levels = sorted(active.values(), key=lambda p: p.audio_level, reverse=True)

        # Ambiguïté si deux participants ont des niveaux trop proches
        if len(levels) >= 2 and levels[0].audio_level - levels[1].audio_level < 0.05:
            return (None, "Participants")

        best = levels[0]
        return (best.endpoint_id, best.display_name)

    # ── Snapshots pour LangGraph ──────────────────────────────────────────────

    def snapshot(self) -> dict:
        """
        Retourne l'état complet de la room.
        Format consommable directement par un agent LangGraph.
        """
        speaker_id, speaker_name = self.current_speaker()
        return {
            "room_participants": {
                eid: {
                    "endpoint_id":    p.endpoint_id,
                    "display_name":   p.display_name,
                    "role":           p.role,
                    "is_muted":       p.is_muted,
                    "is_video_muted": p.is_video_muted,
                    "raised_hand":    p.raised_hand,
                    "audio_level":    round(p.audio_level, 3),
                }
                for eid, p in self._participants.items()
            },
            "dominant_speaker": {
                "endpoint_id":  self._dominant_id,
                "display_name": self._dominant_name,
            },
            "current_speaker": {
                "endpoint_id":  speaker_id,
                "display_name": speaker_name,
            },
            "total_participants": len(self._participants),
        }

    def get_name(self, endpoint_id: str) -> str:
        """Résout endpoint_id → display_name."""
        if endpoint_id in self._participants:
            return self._participants[endpoint_id].display_name
        return endpoint_id

    @property
    def participants(self) -> dict[str, ParticipantInfo]:
        return dict(self._participants)

    @property
    def count(self) -> int:
        return len(self._participants)
