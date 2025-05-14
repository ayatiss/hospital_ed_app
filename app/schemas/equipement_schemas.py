from pydantic import BaseModel
from typing import Optional
class CreateEquipmentSchema(BaseModel):
    name: str
    type: str
    total_quantity: int
    location: Optional[str] = None
    last_maintenance_date: Optional[str] = None
    manufacturer: Optional[str] = None
    purchase_date: Optional[str] = None


class EquipmentResponseSchema(BaseModel):
    equipmentID: int
    name: str
    type: str
    status: str
    total_quantity: int
    available_quantity: int
    location: Optional[str] = None
    last_maintenance_date: Optional[str] = None
    manufacturer: Optional[str] = None
    purchase_date: Optional[str] = None

    class Config:
        orm_mode = True
