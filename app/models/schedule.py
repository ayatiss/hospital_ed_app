from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    scheduleID = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    shiftDetails = Column(String, nullable=True)