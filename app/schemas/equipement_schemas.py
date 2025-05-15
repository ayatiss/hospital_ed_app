from datetime import date
from pydantic import BaseModel
from typing import Optional

class CreateEquipmentSchema(BaseModel):
    name: str
    type: str
    status: Optional[str] = "available"
    total_quantity: Optional[int] = 1
    available_quantity: Optional[int] = 1
    location: Optional[str] = None
    last_maintenance_date: Optional[date] = None
    manufacturer: Optional[str] = None
    purchase_date: date


class EquipmentResponseSchema(BaseModel):
    equipmentID: int
    name: str
    type: str
    status: str
    total_quantity: int
    available_quantity: int
    location: Optional[str] = None
    last_maintenance_date: Optional[date] = None
    manufacturer: Optional[str] = None
    purchase_date: Optional[date] = None

    class Config:
        orm_mode = True
