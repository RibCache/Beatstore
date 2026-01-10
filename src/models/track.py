from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.db.database import Base
from src.models.user import User

class Track(Base):
    __tablename__ = "tracks"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    bpm: Mapped[int]
    genre: Mapped[str]
    price: Mapped[float]
    owner_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    cover_image: Mapped[str]