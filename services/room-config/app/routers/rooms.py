import logging
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import get_settings
from app.schemas.room_config import (
    RoomConfigCreate,
    RoomConfigUpdate,
    RoomConfigResponse,
    RoomReserveRequest,
    AgentContextResponse,
)
from app.schemas.room_history import RoomHistoryResponse
from app.services import room_config_service as svc
from app.services import room_history_service as history_svc

log = logging.getLogger(__name__)
router = APIRouter(prefix="/rooms", tags=["rooms"])
settings = get_settings()


def verify_token(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    if token != settings.API_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalide")
    return token


@router.get("/{room_id}/context", response_model=AgentContextResponse)
def get_agent_context(
    room_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    """
    Endpoint principal utilisé par le peer au démarrage.
    Retourne le contexte complet de l'agent pour cette room.
    Crée une config par défaut si elle n'existe pas — et c'est aussi ICI que
    toute réservation "pending" est promue "confirmed" dès qu'une preuve
    réelle d'usage Jitsi arrive (cf. services/room_config_service.py).
    """
    config = svc.get_or_create_default(db, room_id)
    return svc.build_agent_context(config)


@router.get("/{room_id}/history", response_model=RoomHistoryResponse)
def get_room_history(
    room_id: str,
    limit: int = history_svc.DEFAULT_LIMIT,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    """
    Historique complet et persistant de la réunion (audio transcrit, chat,
    paroles de l'agent). Utilisé par le peer pour se réhydrater — au join
    initial comme après un redémarrage/crash — et retrouver naturellement
    le fil de la réunion en cours.
    """
    entries = history_svc.get_history(db, room_id, limit)
    return RoomHistoryResponse(
        room_id=room_id,
        count=len(entries),
        entries=entries,
        formatted_context=history_svc.format_context(entries),
    )


@router.get("/", response_model=list[RoomConfigResponse])
def list_rooms(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    return svc.list_room_configs(db, skip, limit)


@router.get("/{room_id}", response_model=RoomConfigResponse)
def get_room(
    room_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    config = svc.get_room_config(db, room_id)
    if not config:
        raise HTTPException(status_code=404, detail="Room config introuvable")
    return config


@router.post("/reserve", response_model=RoomConfigResponse, status_code=201)
def reserve_room(
    data: RoomReserveRequest,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    """
    Flux recommandé pour créer une room CIVITAS (cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md
    §3-4) : réserve les métadonnées avec status="pending". Jitsi/Prosody
    n'offrant pas de pré-provisioning de room (Cas A confirmé), le statut ne
    passe à "confirmed" que lorsqu'un événement Jitsi réel est reçu pour ce
    room_id (dès que quelqu'un rejoint effectivement l'URL de la room).
    """
    return svc.reserve_room_config(db, data)


@router.post("/", response_model=RoomConfigResponse, status_code=201)
def create_room(
    data: RoomConfigCreate,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    """
    ⚠️ Legacy — crée une config immédiatement "confirmed" SANS aucune
    vérification qu'une room Jitsi réelle correspond à ce room_id (source de
    "rooms fantômes", cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §2.1). Conservé
    pour rétrocompatibilité uniquement — préférer POST /rooms/reserve pour
    tout nouvel usage.
    """
    return svc.create_room_config(db, data)


@router.patch("/{room_id}", response_model=RoomConfigResponse)
def update_room(
    room_id: str,
    data: RoomConfigUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    config = svc.update_room_config(db, room_id, data)
    if not config:
        raise HTTPException(status_code=404, detail="Room config introuvable")
    return config


@router.delete("/{room_id}", status_code=204)
def delete_room(
    room_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(verify_token),
):
    if not svc.delete_room_config(db, room_id):
        raise HTTPException(status_code=404, detail="Room config introuvable")
