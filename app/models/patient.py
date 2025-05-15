from sqlalchemy import Column, Date, ForeignKey, Integer, String
from app.core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    patientID = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    date_of_birth = Column(String, nullable=True)
    medicalHistory = Column(String, nullable=True)
    currentStatus = Column(String, nullable=True)  # admitted, discharged, under observation
    admission_date = Column(Date, nullable=True)
    discharge_date = Column(Date, nullable=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), nullable=True)
    emergency_contact = Column(String, nullable=True)
    insurance_provider = Column(String, nullable=True)
