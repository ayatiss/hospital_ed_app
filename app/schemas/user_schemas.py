from pydantic import BaseModel, EmailStr
from typing import Optional

from datetime import date


# Login input
class LoginSchema(BaseModel):
    username: str
    password: str


# Token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Create nurse
class CreateNurseSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[date]
    hire_date: Optional[date]
    department: Optional[str] = None
    certifications: Optional[str]
    years_of_experience: Optional[str] = None
    schedule: Optional[str] = None
    is_archived: Optional[bool] = False
    is_available: Optional[bool] = True


# Create doctor
class CreateDoctorSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[date]
    department: Optional[str] = None
    specialization: Optional[str] = None
    license_number: Optional[str] = None
    hire_date: Optional[date]
    years_of_experience: Optional[str] = None
    schedule: Optional[str] = None
    is_archived: Optional[bool] = False
    is_available: Optional[bool] = True


# Create receptionist
class CreateReceptionistSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    date_of_birth: Optional[date]
    number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str]
    gender: Optional[str]
    hire_date: Optional[date]
    desk_location: Optional[str] = None
    languages_spoken: Optional[str] = None
    is_archived: Optional[bool] = False
    is_available: Optional[bool] = True


# Response for user info
class UserResponseSchema(BaseModel):
    userID: int
    username: str
    firstname: str
    lastname: str
    role: str
    number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[date]
    hire_date: Optional[date]
    is_archived: Optional[bool] = False
    is_available: Optional[bool] = True
    class Config:
        orm_mode = True

class DoctorResponseSchema(BaseModel):
    doctorID: int
    department: Optional[str] = None
    specialization: Optional[str] = None
    license_number: Optional[str] = None
    years_of_experience: Optional[str] = None
    schedule: Optional[str] = None
    user: UserResponseSchema

    class Config:
        orm_mode = True

class NurseResponseSchema(BaseModel):
    nurseID: int
    department: Optional[str] = None
    years_of_experience: Optional[str] = None
    schedule: Optional[str] = None
    certifications: Optional[str] = None
    user: UserResponseSchema

    class Config:
        orm_mode = True
class ReceptionistResponseSchema(BaseModel):
    receptionistID: int
    desk_location: Optional[str] = None
    languages_spoken: Optional[str] = None
    user: UserResponseSchema

    class Config:
        orm_mode = True

class UpdateUserBaseSchema(BaseModel):
    firstname: str
    lastname: str
    role: str
    number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[date]
    hire_date: Optional[date]

class UpdateDoctorSchema(UpdateUserBaseSchema):
    department: Optional[str]
    schedule: Optional[str]
    specialization: Optional[str]
    license_number: Optional[str]
    years_of_experience: Optional[int]

class UpdateNurseSchema(UpdateUserBaseSchema):
    department: Optional[str]
    schedule: Optional[str]
    years_of_experience: Optional[str]
    certifications: Optional[str]

class UpdateReceptionistSchema(UpdateUserBaseSchema):
    desk_location: Optional[str]
    languages_spoken: Optional[str]