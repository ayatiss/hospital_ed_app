from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.services.auth import get_user_from_token, login_user
from app.core.dependencies import get_db
from app.schemas.user_schemas import LoginSchema, TokenResponse, UserResponseSchema

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(db, login_data.username, login_data.password)

@router.get("/me", response_model=UserResponseSchema)
def get_me(Authorization: str = Header(...), db: Session = Depends(get_db)):
    token = Authorization.split(" ")[1]  # Extract token after "Bearer"
    user = get_user_from_token(db, token)
    return user


