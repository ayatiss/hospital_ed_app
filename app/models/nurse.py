from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.user import User

class Nurse(User):
    __tablename__ = "nurses"

    nurseID = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    is_archived = Column(Boolean, default=False)
    userID = Column(Integer, ForeignKey("users.userID"))

    __mapper_args__ = {
        "polymorphic_identity": "nurse",
    }