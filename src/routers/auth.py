from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.crud import create_user
from src.schemas.user import UserResponse, CreateUser
from src.db.database import get_db
from src.models.user import User


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def user_create_route(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db=db, user=user)