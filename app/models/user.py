from sqlalchemy import Column, Date, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    number = Column(String, nullable=True)  # phone number
    email = Column(String, nullable=True, unique=True)
    hashed_password = Column(String, nullable=False)
    address = Column(String, nullable=True)
    gender = Column(String, nullable=True)  # male, female, other
    date_of_birth = Column(Date, nullable=True)
    hire_date = Column(Date, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role,
    }

