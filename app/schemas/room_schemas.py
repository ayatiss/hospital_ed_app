from pydantic import BaseModel
from typing import Optional
class CreateRoomSchema(BaseModel):
    name: str
    type: str
    status: str
    capacity: Optional[int] = 1
    floor: Optional[int] = None
    wing: Optional[str] = None


class RoomResponseSchema(BaseModel):
    room_id: int
    name: str
    type: str
    status: str
    capacity: int
    floor: Optional[int] = None
    wing: Optional[str] = None

    class Config:
        orm_mode = True
