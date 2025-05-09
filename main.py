from fastapi import FastAPI, Depends
from app.core.database import SessionLocal

from app.core.database import Base, engine
from app.models import user  # make sure your model is imported

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
