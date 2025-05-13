from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth import login_user
from app.core.dependencies import get_db
from app.schemas.user_schemas import LoginSchema, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(db, login_data.username, login_data.password)

