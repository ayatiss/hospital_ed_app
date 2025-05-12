from sqlalchemy import Column, Integer, ForeignKey
from app.models.user import User

class Receptionist(User):
    __tablename__ = "receptionists"

    receptionistID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))

    __mapper_args__ = {
        "polymorphic_identity": "receptionist",
    }