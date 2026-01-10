from sqlalchemy.orm import Session
from src.models.user import User
from src.models.track import Track
from src.schemas.track import CreateTrack
from src.schemas.user import CreateUser
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def create_user(user: CreateUser, db: Session):
    hashed_password = pwd_context.hash(user.password)
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
