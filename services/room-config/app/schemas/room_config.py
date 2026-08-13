from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field


class RoomConfigCreate(BaseModel):
    room_id: str
    agent_name: str = "CIVITAS"
    system_prompt: str = ""
    behavior_mode: str = Field(default="on_call", pattern="^(on_call|proactive|silent)$")
    language: str = "fr"
    can_speak: bool = True
    can_write_chat: bool = True
    can_use_tools: bool = False
    can_use_rag: bool = False
    can_moderate: bool = False
    peer_enabled: bool = True
    invocation_keywords: list[str] = ["civitas"]
    tools_allowed: list[str] = []
    extra_config: dict[str, Any] = {}
    is_active: bool = True


class RoomConfigUpdate(BaseModel):
    agent_name: str | None = None
    system_prompt: str | None = None
    behavior_mode: str | None = None
    language: str | None = None
    can_speak: bool | None = None
    can_write_chat: bool | None = None
    can_use_tools: bool | None = None
    can_use_rag: bool | None = None
    can_moderate: bool | None = None
    peer_enabled: bool | None = None
    invocation_keywords: list[str] | None = None
    tools_allowed: list[str] | None = None
    extra_config: dict[str, Any] | None = None
    is_active: bool | None = None


class RoomConfigResponse(BaseModel):
    room_id: str
    agent_name: str
    system_prompt: str
    behavior_mode: str
    language: str
    can_speak: bool
    can_write_chat: bool
    can_use_tools: bool
    can_use_rag: bool
    can_moderate: bool
    peer_enabled: bool
    invocation_keywords: list[str]
    tools_allowed: list[str]
    extra_config: dict[str, Any]
    is_active: bool
    # Traçabilité room réelle Jitsi — cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §1-4.
    # Champs en lecture seule : jamais fournis par l'appelant (RoomConfigCreate/
    # Update), gérés uniquement par room-config lui-même (POST /rooms/reserve
    # et le consumer Kafka de confirmation).
    status: Literal["pending", "confirmed"]
    source: str
    jitsi_confirmed_at: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class AgentContextResponse(BaseModel):
    room_id: str
    agent_name: str
    system_prompt: str
    behavior_mode: str
    language: str
    permissions: dict[str, bool]
    invocation_keywords: list[str]
    tools_allowed: list[str]


class RoomReserveRequest(BaseModel):
    """
    Réservation d'une room CIVITAS AVANT que la room Jitsi réelle existe.
    Statut "pending" jusqu'à réception d'un événement Jitsi réel confirmant
    que la room a effectivement été créée côté Prosody (muc-room-created) —
    cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §3-4 (Cas A : création implicite
    Jitsi, aucune API de pré-provisioning n'existe côté Jicofo/Prosody
    vanilla). Mêmes champs de configuration que RoomConfigCreate.
    """
    room_id: str
    agent_name: str = "CIVITAS"
    system_prompt: str = ""
    behavior_mode: str = Field(default="on_call", pattern="^(on_call|proactive|silent)$")
    language: str = "fr"
    can_speak: bool = True
    can_write_chat: bool = True
    can_use_tools: bool = False
    can_use_rag: bool = False
    can_moderate: bool = False
    peer_enabled: bool = True
    invocation_keywords: list[str] = ["civitas"]
    tools_allowed: list[str] = []
    extra_config: dict[str, Any] = {}
