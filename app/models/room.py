from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Room(Base):
    __tablename__ = "rooms"

    roomID = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # ICU, Surgery, etc.
    status = Column(String, nullable=False)  # available, occupied, maintenance
    capacity = Column(Integer, nullable=False, default=1)
    floor = Column(Integer, nullable=True)
    wing = Column(String, nullable=True)
