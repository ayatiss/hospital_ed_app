from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Equipment(Base):
    __tablename__ = "equipment"

    equipmentID = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    availability = Column(String, nullable=False)