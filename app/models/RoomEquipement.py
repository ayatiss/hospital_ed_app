from sqlalchemy import Column, ForeignKey, Integer
from app.core.database import Base


class RoomEquipment(Base):
    __tablename__ = "room_equipment"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.roomID"))
    equipment_id = Column(Integer, ForeignKey("equipment.equipmentID"))
    quantity_assigned = Column(Integer, nullable=False)
