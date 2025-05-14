from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.user import User

class Nurse(User):
    __tablename__ = "nurses"

    nurseID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    certifications = Column(String, nullable=True)  # comma-separated list
    is_archived = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)
    __mapper_args__ = {
        "polymorphic_identity": "nurse",
    }
