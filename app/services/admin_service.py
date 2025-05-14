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
    hashed = hash_password(nurse_data.password)

    new_nurse = Nurse(
        username=nurse_data.username,
        firstname=nurse_data.firstname,
        lastname=nurse_data.lastname,
        hashed_password=hashed,  
        role="nurse",
        department=nurse_data.department,
        schedule=nurse_data.schedule,
        number=nurse_data.number,
        email=nurse_data.email,   
        address=nurse_data.address,
        gender=nurse_data.gender,
        date_of_birth=nurse_data.date_of_birth,
        hire_date=nurse_data.hire_date,
        years_of_experience=nurse_data.years_of_experience, 
        is_archived=nurse_data.is_archived,
        is_available=nurse_data.is_available
    )
    
    db.add(new_nurse)
    db.commit()
    db.refresh(new_nurse)
    return new_nurse


# Create doctor logic
def create_doctor(db: Session, doctor_data: CreateDoctorSchema) -> Doctor:
    hashed = hash_password(doctor_data.password)
    new_doctor = Doctor(
        username=doctor_data.username,
        firstname=doctor_data.firstname,
        lastname=doctor_data.lastname,
        hashed_password=hashed,  
        role="doctor",
        department=doctor_data.department,
        schedule=doctor_data.schedule,
        number=doctor_data.number,
        email=doctor_data.email,
        address=doctor_data.address,
        gender=doctor_data.gender,
        specialization=doctor_data.specialization,
        license_number=doctor_data.license_number,
        years_of_experience=doctor_data.years_of_experience,
        is_archived=doctor_data.is_archived,
        is_available=doctor_data.is_available
    )
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


# Create receptionist logic
def create_receptionist(db: Session, receptionist_data: CreateReceptionistSchema) -> Receptionist:
    hashed = hash_password(receptionist_data.password)
    new_receptionist = Receptionist(
        username=receptionist_data.username,
        firstname=receptionist_data.firstname,
        lastname=receptionist_data.lastname,
        hashed_password=hashed,  
        role="receptionist",
        number=receptionist_data.number,
        email=receptionist_data.email,
        address=receptionist_data.address,
        gender=receptionist_data.gender,
        desk_location=receptionist_data.desk_location,
        languages_spoken=receptionist_data.languages_spoken
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
