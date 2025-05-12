from fastapi import FastAPI, Depends
from app.core.database import SessionLocal

from app.core.database import Base, engine
from app.models import user  # make sure your model is imported
from app.models import admin
from app.models import doctor
from app.models import equipement
from app.models import nurse
from app.models import patient
from app.models import receptionist
from app.models import room
from app.models import schedule
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
