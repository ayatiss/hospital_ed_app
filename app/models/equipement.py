from sqlalchemy import Column, Date, Integer, String
from app.core.database import Base

class Equipment(Base):
    __tablename__ = "equipments"

    equipmentID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # e.g., Ventilator
    type = Column(String, nullable=False)  # diagnostic, life-support, etc.
    status = Column(String, nullable=False, default="available")
    total_quantity = Column(Integer, nullable=False, default=1)
    available_quantity = Column(Integer, nullable=False, default=1)
    location = Column(String, nullable=True)
    last_maintenance_date = Column(Date, nullable=True)
    manufacturer = Column(String, nullable=True)
    purchase_date = Column(Date, nullable=True)
