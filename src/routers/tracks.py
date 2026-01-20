from src.services import track
from src.schemas.track import CreateTrack
from src.models.user import User
from src.repositories.track import TrackRepository
from src.db.database import get_db
from src.routers.auth import get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tracks")
def create_track_route(
    track_in: CreateTrack,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = TrackRepository(db)
    
    return track.track_create_service(repo, track_in, current_user.id)

@router.delete("/{track_id}", status_code=204)
def delete_track(
    track_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = TrackRepository(db)
    track.delete_track_service(repo, track_id, current_user.id)
    return
    

