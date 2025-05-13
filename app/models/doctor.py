from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.user import User

class Doctor(User):
    __tablename__ = "doctors"

    doctorID = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    is_archived = Column(Boolean, default=False)
    __mapper_args__ = {
        "polymorphic_identity": "doctor",
    }