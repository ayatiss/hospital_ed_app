from fastapi import APIRouter, Depends
from app.schemas import UserResponseSchema
from app.services.user_service import get_current_user

router = APIRouter()

@router.get("/api/get_user", response_model=UserResponseSchema)
def read_current_user(current_user = Depends(get_current_user)):
    return current_user