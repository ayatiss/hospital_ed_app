from sqlalchemy.orm import Session
from app.models.user import User
from app.models.admin import Admin
from app.models.nurse import Nurse
from app.models.doctor import Doctor
from app.models.receptionist import Receptionist
from app.schemas.user_schemas import CreateNurseSchema, CreateDoctorSchema, CreateReceptionistSchema
from app.services.auth import hash_password
from fastapi import HTTPException

# Create nurse logic
def create_nurse(db: Session, nurse_data: CreateNurseSchema) -> Nurse:
    hashed_password = hash_password(nurse_data.password)
    new_nurse = Nurse(
        username=nurse_data.username,
        firstname=nurse_data.firstname,
        lastname=nurse_data.lastname,
        password=hashed_password,
        department=nurse_data.department,
        schedule=nurse_data.schedule,
        number=nurse_data.number,
        email=nurse_data.email
    )
    db.add(new_nurse)
    db.commit()
    db.refresh(new_nurse)
    return new_nurse


# Create doctor logic
def create_doctor(db: Session, doctor_data: CreateDoctorSchema) -> Doctor:
    hashed_password = hash_password(doctor_data.password)
    new_doctor = Doctor(
        username=doctor_data.username,
        firstname=doctor_data.firstname,
        lastname=doctor_data.lastname,
        password=hashed_password,
        department=doctor_data.department,
        schedule=doctor_data.schedule,
        number=doctor_data.number,
        email=doctor_data.email
    )
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


# Create receptionist logic
def create_receptionist(db: Session, receptionist_data: CreateReceptionistSchema) -> Receptionist:
    hashed_password = hash_password(receptionist_data.password)
    new_receptionist = Receptionist(
        username=receptionist_data.username,
        firstname=receptionist_data.firstname,
        lastname=receptionist_data.lastname,
        password=hashed_password,
        number=receptionist_data.number,
        email=receptionist_data.email
    )
    db.add(new_receptionist)
    db.commit()
    db.refresh(new_receptionist)
    return new_receptionist


# Archive user logic
def archive_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.userID == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_archived = True
    db.commit()
    db.refresh(user)
    return user
