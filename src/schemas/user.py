from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
   username: str
   email: EmailStr
   password: str
   is_producer: bool = False
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_producer: bool
    
    class Config:
        from_attributes = True