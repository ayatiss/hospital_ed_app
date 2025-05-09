from fastapi import FastAPI, Depends
from app.core.database import SessionLocal


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
