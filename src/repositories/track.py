from sqlalchemy.orm import Session 
from src.models.track import Track
from src.schemas.track import CreateTrack

class TrackRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def track_id_check(self, track_id: int):
        return self.db.query(Track).filter(Track.id == track_id).first()
        
    def create_track(self, track_data: CreateTrack, owner_id: int):
        new_track = Track(
            **track_data,
            owner_id=owner_id,
            cover_image="default.jpg"
        )
        self.db.add(new_track)
        self.db.commit()
        self.db.refresh(new_track)
        
        return new_track
    
    def get_all_tracks(self):
        return self.db.query(Track).all()
    
    def get_track_by_id(self, track_id: int):
        return self.track_id_check(track_id)