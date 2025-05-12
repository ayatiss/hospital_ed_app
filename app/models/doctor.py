from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.user import User

class Doctor(User):
    __tablename__ = "doctors"

    doctorID = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    userID = Column(Integer, ForeignKey("users.userID"))

    __mapper_args__ = {
        "polymorphic_identity": "doctor",
    }