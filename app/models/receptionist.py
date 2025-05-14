from sqlalchemy import Column, Integer, ForeignKey, String
from app.models.user import User

class Receptionist(User):
    __tablename__ = "receptionists"

    receptionistID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    desk_location = Column(String, nullable=True)
    languages_spoken = Column(String, nullable=True)  # e.g., "English, Spanish"

    __mapper_args__ = {
        "polymorphic_identity": "receptionist",
    }