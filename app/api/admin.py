from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.services.admin_service import create_nurse, create_doctor, create_receptionist, archive_user
from app.core.dependencies import get_db, get_current_admin
from app.schemas.user_schemas import CreateNurseSchema, CreateDoctorSchema, CreateReceptionistSchema, DoctorResponseSchema, NurseResponseSchema, ReceptionistResponseSchema, UserResponseSchema

router = APIRouter()

# Admin: Create nurse
@router.post("/create-nurse", response_model=NurseResponseSchema)
def create_nurse_endpoint(
    nurse_data: CreateNurseSchema,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return create_nurse(db, nurse_data)


# Admin: Create doctor
@router.post("/create-doctor", response_model=DoctorResponseSchema)
def create_doctor_endpoint(doctor_data: CreateDoctorSchema, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return create_doctor(db, doctor_data)


# Admin: Create receptionist
@router.post("/create-receptionist", response_model=ReceptionistResponseSchema)
def create_receptionist_endpoint(receptionist_data: CreateReceptionistSchema, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return create_receptionist(db, receptionist_data)


# Admin: Archive user
@router.put("/archive/{user_id}", response_model=UserResponseSchema)
def archive_user_endpoint(user_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return archive_user(db, user_id)
