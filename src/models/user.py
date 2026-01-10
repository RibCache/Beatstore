from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base
from datetime import datetime

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
    created_at: Mapped[datetime]
    