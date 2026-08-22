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
    # Contrôle modérateur manuel (inject/eject) — colonne dédiée, propre.
    # AVANT : écrit dans extra_config.peer_enabled (set_peer_enabled) mais lu
    # depuis permissions.peer_enabled (is_peer_enabled), qui n'existait nulle
    # part -> l'éjection manuelle d'un peer ne "tenait" jamais (cf. §2.3/§7.5
    # PLAN_SYNCHRONISATION_ROOMS_JITSI.md). L'ancienne écriture remplaçait
    # aussi TOUT extra_config au passage (perte de données silencieuse).
    peer_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    # Successeur de peer_enabled — CIVITAS Agent Runtime remplace le peer
    # (cf. docs/architecture/, en particulier 04-plan-migration.md "Migration
    # du schéma room_configs"). Colonne ADDITIVE : coexiste avec peer_enabled
    # tant que services/room-spawner (déprécié) et services/civitas-orchestrator
    # tournent en parallèle pendant la bascule progressive — les deux colonnes
    # sont synchronisées applicativement à chaque écriture (jamais par
    # trigger SQL) par app/services/room_config_service.py::_sync_agent_peer_enabled.
    # peer_enabled sera supprimée en Phase 6 du plan de migration, une fois
    # room-spawner désactivé (migration Alembic B, non encore écrite : elle ne
    # le sera qu'à ce moment-là, pas par anticipation).
    agent_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    invocation_keywords: Mapped[list] = mapped_column(JSON, default=lambda: ["civitas"])
    tools_allowed: Mapped[list] = mapped_column(JSON, default=list)
    extra_config: Mapped[dict] = mapped_column(JSON, default=dict)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Traçabilité room réelle Jitsi — cf. §1-4 PLAN_SYNCHRONISATION_ROOMS_JITSI.md.
    # status="pending" : réservée côté CIVITAS, room Jitsi réelle pas encore
    #   confirmée (créée via POST /rooms/reserve, cf. routers/rooms.py).
    # status="confirmed" : soit un événement Jitsi réel (muc-room-created) a
    #   été reçu pour ce room_id, soit c'est une ligne créée avant l'existence
    #   de ce statut (défaut historique, non vérifiable rétroactivement).
    status: Mapped[str] = mapped_column(String(20), default="confirmed")
    # manager_api_legacy | manager_api_reserved | jitsi_event
    source: Mapped[str] = mapped_column(String(50), default="manager_api_legacy")
    jitsi_confirmed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
