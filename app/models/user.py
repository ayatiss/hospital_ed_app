from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role,
    }
