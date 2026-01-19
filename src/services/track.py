from src.repositories.track import TrackRepository
from src.schemas.track import CreateTrack
from fastapi import HTTPException

def track_create_service(repo: TrackRepository, track_in: CreateTrack, user_id:int):
    track_dict = track_in.model_dump()
    return repo.create_track(track_dict, user_id)

def get_track_id_service(repo: TrackRepository, track_id: int):
    track = repo.get_track_by_id(track_id)
    
    if not track:
        raise HTTPException(status_code=404)
    
    return track
    