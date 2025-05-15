from datetime import date
from pydantic import BaseModel
from typing import Optional


class CreatePatientSchema(BaseModel):
    firstname: str
    lastname: str
    gender: Optional[str]
    date_of_birth: Optional[str]
    medicalHistory: Optional[str]
    currentStatus: Optional[str]
    admission_date: Optional[date]
    discharge_date: Optional[date]
    room_id: Optional[int]
    emergency_contact: Optional[str]
    insurance_provider: Optional[str]


class UpdatePatientSchema(BaseModel):
    firstname: str
    lastname: str
    gender: Optional[str]
    date_of_birth: Optional[str]
    medicalHistory: Optional[str]
    currentStatus: Optional[str]
    admission_date: Optional[date]
    discharge_date: Optional[date]
    room_id: Optional[int]
    emergency_contact: Optional[str]
    insurance_provider: Optional[str]


class PatientResponseSchema(BaseModel):
    patientID: int
    firstname: str
    lastname: str
    gender: Optional[str]
    date_of_birth: Optional[str]
    medicalHistory: Optional[str]
    currentStatus: Optional[str]
    admission_date: Optional[date]
    discharge_date: Optional[date]
    room_id: Optional[int]
    emergency_contact: Optional[str]
    insurance_provider: Optional[str]
    class Config:
        orm_mode = True
