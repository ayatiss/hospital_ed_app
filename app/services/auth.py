from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.user_schemas import TokenResponse

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        print("Password verification error:", e)
        raise HTTPException(status_code=500, detail="Password verification failed")

def create_access_token(data: dict) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user_from_token(db: Session, token: str) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print("Incoming token:", token)  # NEW DEBUG
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Decoded payload:", payload)  # NEW DEBUG

        user_id_str = payload.get("sub")
        if not user_id_str:
            print("No 'sub' in payload")  # NEW DEBUG
            raise credentials_exception
        user_id = int(user_id_str)
        print("Extracted user_id:", user_id)  # NEW DEBUG

    except (JWTError, ValueError, TypeError) as e:
        print("Token decode error:", e)  # NEW DEBUG
        raise credentials_exception

    user = db.query(User).filter(User.userID == user_id).first()
    if user is None:
        print("No user found for ID", user_id)  # NEW DEBUG
        raise credentials_exception

    print("User from token:", user.username, "| role:", user.role)  # NEW DEBUG
    return user


def login_user(db: Session, username: str, password: str) -> TokenResponse:
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=400, detail="Incorrect username or password"
        )

    # Create token
    token_payload = {"sub": str(user.userID)}
    print("Token payload:", token_payload)  # DEBUG: Check payload before encoding

    token = create_access_token(data=token_payload)
    print("Generated JWT token:", token)  # DEBUG: Check token string

    return TokenResponse(access_token=token)

