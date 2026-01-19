from src.services import track
from src.schemas.track import CreateTrack
from src.models.user import User
from src.repositories.track import TrackRepository
from src.db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tracks")
def create_track_route(
    track_in: CreateTrack,
    db: Session = Depends(get_db)
):
    repo = TrackRepository(db)
    
    return track.track_create_service(repo, track_in, user_id=1)
    

