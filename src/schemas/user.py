from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
   username: str
   email: EmailStr
   password: str
   
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    class Config:
        from_attributes = True