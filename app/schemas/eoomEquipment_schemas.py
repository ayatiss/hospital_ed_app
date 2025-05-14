from pydantic import BaseModel
from typing import Optional

class AssignEquipmentSchema(BaseModel):
    room_id: int
    equipment_id: int
    quantity: int


class RoomEquipmentResponseSchema(BaseModel):
    id: int
    room_id: int
    equipment_id: int
    quantity_assigned: int

    class Config:
        orm_mode = True
