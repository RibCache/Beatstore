from pydantic import BaseModel

class CreateTrack(BaseModel):
    title: str
    bpm: int
    genre: str
    price: float
    
class TrackResponse(BaseModel):
    id: int
    owner_id: int
    title: str
    bpm: int
    genre: str
    price: float
    
    class Config:
        from_attributes = True