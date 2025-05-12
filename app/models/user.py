from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    contactInfo = Column(String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role,
    }