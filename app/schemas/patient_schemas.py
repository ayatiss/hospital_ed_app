from pydantic import BaseModel
from typing import Optional


class CreatePatientSchema(BaseModel):
    medicalHistory: Optional[str] = None
    currentStatus: Optional[str] = None


class UpdatePatientSchema(BaseModel):
    medicalHistory: Optional[str] = None
    currentStatus: Optional[str] = None


class PatientResponseSchema(BaseModel):
    patientID: int
    medicalHistory: Optional[str] = None
    currentStatus: Optional[str] = None

    class Config:
        orm_mode = True
