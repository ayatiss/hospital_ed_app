from sqlalchemy import Column, ForeignKey, Integer
from app.core.database import Base


class RoomEquipment(Base):
    __tablename__ = "room_equipment"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    equipment_id = Column(Integer, ForeignKey("equipments.equipmentID"))
    quantity_assigned = Column(Integer, nullable=False)
