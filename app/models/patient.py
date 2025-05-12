from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    patientID = Column(Integer, primary_key=True, index=True)
    medicalHistory = Column(String, nullable=True)
    currentStatus = Column(String, nullable=True)