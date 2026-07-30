from datetime import datetime
from pydantic import BaseModel


class RoomHistoryEntryResponse(BaseModel):
    speaker_id: str | None = None
    speaker_name: str
    entry_type: str
    text: str
    occurred_at: datetime

    model_config = {"from_attributes": True}


class RoomHistoryResponse(BaseModel):
    room_id: str
    count: int
    entries: list[RoomHistoryEntryResponse]
    # Rendu texte prêt à injecter tel quel dans le contexte de l'agent —
    # évite de dupliquer la logique de formatage côté peer.
    formatted_context: str
