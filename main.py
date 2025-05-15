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
from app.models import RoomEquipement
from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(admin_router, prefix="/api/admin")
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
