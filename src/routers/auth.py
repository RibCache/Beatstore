from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.services.crud import create_user
from src.schemas.user import UserResponse, CreateUser
from src.db.database import get_db
from src.models.user import User
from src.core.security import verify_password, create_access_token, decode_access_token, oauth2_scheme


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def user_create_route(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db=db, user=user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
        
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    email = decode_access_token(token)
    if email is None:
        raise HTTPException(
            status_code=401
        )
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user