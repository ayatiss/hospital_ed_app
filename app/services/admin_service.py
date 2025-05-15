from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Boolean, cast, or_
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.admin import Admin
from app.models.nurse import Nurse
from app.models.doctor import Doctor
from app.models.receptionist import Receptionist
from app.schemas.user_schemas import CreateNurseSchema, CreateDoctorSchema, CreateReceptionistSchema, UpdateDoctorSchema, UpdateNurseSchema, UpdateReceptionistSchema
from app.services.auth import hash_password
from fastapi import HTTPException
from sqlalchemy.orm import aliased, joinedload
from app.models.RoomEquipement import RoomEquipment
from app.models.equipement import Equipment
from app.models.patient import Patient
from app.models.room import Room
from app.schemas.equipement_schemas import CreateEquipmentSchema
from app.schemas.room_schemas import CreateRoomSchema

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
        languages_spoken=receptionist_data.languages_spoken,
        is_archived=receptionist_data.is_archived,
        is_available=receptionist_data.is_available
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

#Edit User Details
def update_user_details(db: Session, user_id: int, update_data: BaseModel) -> User:
    user = db.query(User).filter(User.userID == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update shared user fields
    for key, value in update_data.dict(exclude_unset=True).items():
        if hasattr(user, key):
            setattr(user, key, value)

    # Update role-specific fields
    if user.role == "doctor" and isinstance(update_data, UpdateDoctorSchema):
        doctor = db.query(Doctor).filter(Doctor.userID == user_id).first()
        for key, value in update_data.dict(exclude_unset=True).items():
            if hasattr(doctor, key):
                setattr(doctor, key, value)

    elif user.role == "nurse" and isinstance(update_data, UpdateNurseSchema):
        nurse = db.query(Nurse).filter(Nurse.userID == user_id).first()
        for key, value in update_data.dict(exclude_unset=True).items():
            if hasattr(nurse, key):
                setattr(nurse, key, value)

    elif user.role == "receptionist" and isinstance(update_data, UpdateReceptionistSchema):
        receptionist = db.query(Receptionist).filter(Receptionist.userID == user_id).first()
        for key, value in update_data.dict(exclude_unset=True).items():
            if hasattr(receptionist, key):
                setattr(receptionist, key, value)

    db.commit()
    db.refresh(user)
    return user


#add equipements 
def create_equipment(db: Session, equipment_data: CreateEquipmentSchema) -> Equipment:
    equipment = Equipment(**equipment_data.dict())
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment

def search_equipments_by_keyword(db: Session, keyword: str):
    query = db.query(Equipment).filter(
        or_(
            Equipment.name.ilike(f"%{keyword}%"),
            Equipment.type.ilike(f"%{keyword}%"),
            Equipment.status.ilike(f"%{keyword}%"),
            Equipment.location.ilike(f"%{keyword}%"),
            Equipment.manufacturer.ilike(f"%{keyword}%")
        )
    )
    return query.all()

def get_all_equipments(db: Session):
    return db.query(Equipment).all()

def get_equipment_by_id(equipment_id: int, db: Session):
    equipment = db.query(Equipment).filter(Equipment.equipmentID == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

#Monitor Patient Admissions/Discharges
def get_patient_statistics(db: Session) -> dict:
    total_patients = db.query(Patient).count()
    admitted = db.query(Patient).filter(Patient.currentStatus == "admitted").count()
    discharged = db.query(Patient).filter(Patient.currentStatus == "discharged").count()
    return {
        "total": total_patients,
        "admitted": admitted,
        "discharged": discharged
    }

#Assign Equipment to Room
def assign_equipment_to_room(db: Session, room_id: int, equipment_id: int, quantity: int):
    room = db.query(Room).filter(Room.room_id == room_id).first()
    equipment = db.query(Equipment).filter(Equipment.equipmentID == equipment_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")

    if equipment.available_quantity < quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Only {equipment.available_quantity} units available"
        )

    # Check if already assigned
    assignment = db.query(RoomEquipment).filter_by(room_id=room_id, equipment_id=equipment_id).first()

    if assignment:
        assignment.quantity_assigned += quantity
    else:
        assignment = RoomEquipment(
            room_id=room_id,
            equipment_id=equipment_id,
            quantity_assigned=quantity
        )
        db.add(assignment)

    # Update available quantity in Equipment
    equipment.available_quantity -= quantity

    db.commit()
    return {"message": "Equipment assigned successfully"}

def unassign_equipment_from_room(db: Session, room_id: int, equipment_id: int, quantity: int):
    assignment = db.query(RoomEquipment).filter_by(room_id=room_id, equipment_id=equipment_id).first()
    equipment = db.query(Equipment).filter(Equipment.equipmentID == equipment_id).first()

    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    if assignment.quantity_assigned < quantity:
        raise HTTPException(status_code=400, detail="Cannot unassign more than assigned")

    assignment.quantity_assigned -= quantity
    equipment.available_quantity += quantity

    if assignment.quantity_assigned == 0:
        db.delete(assignment)

    db.commit()
    return {"message": "Equipment unassigned successfully"}

# ------------------------- PATIENT SERVICES -------------------------
def get_all_patients(db: Session) -> List[Patient]:
    return db.query(Patient).all()

def get_today_patients(db: Session) -> List[Patient]:
    today = date.today().isoformat()
    return db.query(Patient).filter(Patient.admission_date == today).all()

def get_patient_by_id(db: Session, patient_id: int) -> Optional[Patient]:
    return db.query(Patient).filter(Patient.patientID == patient_id).first()

def search_patients(db: Session, keyword: str) -> List[Patient]:
    return db.query(Patient).filter(
        (Patient.firstname.ilike(f"%{keyword}%")) |
        (Patient.lastname.ilike(f"%{keyword}%"))
    ).all()

# ------------------------- DOCTOR SERVICES -------------------------
def get_all_doctors(db: Session):
    user_alias = aliased(User)
    return (
        db.query(Doctor)
        .join(user_alias, Doctor.user)
        .options(joinedload(Doctor.user))  # eager-load the user relation
        .filter(cast(user_alias.is_archived, Boolean) == False)
        .all()
    )

def get_available_doctors(db: Session) -> List[Doctor]:
    user_alias = aliased(User)
    return (
        db.query(Doctor)
        .join(user_alias, Doctor.user)
        .options(joinedload(Doctor.user))  # eager-load the user relation
        .filter(cast(user_alias.is_archived, Boolean) == False, cast(user_alias.is_available, Boolean) == True)
        .all()
    )
   
def get_doctor_by_id(db: Session, doctor_id: int) -> Optional[Doctor]:
    return db.query(Doctor).filter(Doctor.doctorID == doctor_id).first()


# ------------------------- NURSE SERVICES -------------------------
def get_all_nurses(db: Session) -> List[Nurse]:
    user_alias = aliased(User)
    return (
        db.query(Nurse)
        .join(user_alias, Nurse.user)
        .options(joinedload(Nurse.user))  # eager-load the user relation
        .filter(cast(user_alias.is_archived, Boolean) == False)
        .all()
    )
def get_available_nurses(db: Session) -> List[Nurse]:
    user_alias = aliased(User)
    return (
        db.query(Nurse)
        .join(user_alias, Nurse.user)
        .options(joinedload(Nurse.user))  # eager-load the user relation
        .filter(cast(user_alias.is_archived, Boolean) == False, cast(user_alias.is_available, Boolean) == True)
        .all()
    )

def get_nurse_by_id(db: Session, nurse_id: int) -> Optional[Nurse]:
    return db.query(Nurse).filter(Nurse.nurseID == nurse_id).first()


# ------------------------- RECEPTIONIST SERVICES -------------------------
def get_all_receptionists(db: Session) -> List[Receptionist]:
    user_alias = aliased(User)
    return (
        db.query(Receptionist)
        .join(user_alias, Receptionist.user)
        .options(joinedload(Receptionist.user))  # eager-load the user relation
        .filter(cast(user_alias.is_archived, Boolean) == False)
        .all()
    )

def get_receptionist_by_id(db: Session, receptionist_id: int) -> Optional[Receptionist]:
    return db.query(Receptionist).filter(Receptionist.receptionistID == receptionist_id).first()


# ------------------------- ROOM SERVICES -------------------------
def create_room(db: Session, room_data: CreateRoomSchema) -> Room:
    room = Room(**room_data.dict())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def get_available_rooms(db: Session) -> List[Room]:
    return db.query(Room).filter(Room.status == "available").all()