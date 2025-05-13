from pydantic import BaseModel, EmailStr
from typing import Optional


# Login input
class LoginSchema(BaseModel):
    username: str
    password: str


# Token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


#  Create nurse
class CreateNurseSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    department: Optional[str] = None
    schedule: Optional[str] = None
    number: Optional[str] = None
    email: Optional[EmailStr] = None


# Create doctor
class CreateDoctorSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    department: Optional[str] = None
    schedule: Optional[str] = None
    number: Optional[str] = None
    email: Optional[EmailStr] = None


#Create receptionist
class CreateReceptionistSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    number: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponseSchema(BaseModel):
    userID: int
    username: str
    firstname: str
    lastname: str
    role: str
    number: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True
