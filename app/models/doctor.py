from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.user import User

class Doctor(User):
    __tablename__ = "doctors"

    doctorID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    specialization = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    years_of_experience = Column(Integer, nullable=True)
    is_archived = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)
    __mapper_args__ = {
        "polymorphic_identity": "doctor",
    }
