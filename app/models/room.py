from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Room(Base):
    __tablename__ = "rooms"

    roomID = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)