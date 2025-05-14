from sqlalchemy import Column, Integer, ForeignKey
from app.models.user import User

class Admin(User):
    __tablename__ = "admins"

    adminID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))

    __mapper_args__ = {
        "polymorphic_identity": "admin",
    }

