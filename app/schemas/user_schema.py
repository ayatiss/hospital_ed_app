from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    role: str
    contactInfo: str | None = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    userID: int

    class Config:
        orm_mode = True
