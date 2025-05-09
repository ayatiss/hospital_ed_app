from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # e.g., 'admin', 'doctor', 'nurse'
    contactInfo = Column(String, nullable=True)

