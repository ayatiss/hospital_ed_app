from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.user import User
from app.services.admin_service import assign_equipment_to_room, create_equipment, create_nurse, create_doctor, create_receptionist, archive_user, create_room, get_all_doctors, get_all_equipments, get_all_nurses, get_all_patients, get_all_receptionists, get_available_doctors, get_available_nurses, get_available_rooms, get_doctor_by_id, get_nurse_by_id, get_patient_by_id, get_patient_statistics, get_receptionist_by_id, get_today_patients, search_equipments_by_keyword, search_patients, unassign_equipment_from_room, update_user_details,get_equipment_by_id
from app.core.dependencies import get_db, get_current_admin
from app.schemas.user_schemas import CreateNurseSchema, CreateDoctorSchema, CreateReceptionistSchema, DoctorResponseSchema, NurseResponseSchema, ReceptionistResponseSchema, UpdateUserBaseSchema, UserResponseSchema
from app.schemas.equipement_schemas import CreateEquipmentSchema, EquipmentResponseSchema
from app.schemas.patient_schemas import PatientResponseSchema
from app.schemas.room_schemas import CreateRoomSchema, RoomResponseSchema
from app.models.doctor import Doctor
from app.models.nurse import Nurse
from app.models.receptionist import Receptionist

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

# -------------------- USER ENDPOINTS --------------------
@router.put("/users/{user_id}", response_model=UserResponseSchema)
def update_user(user_id: int, update_data: UpdateUserBaseSchema, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return update_user_details(db, user_id, update_data)

# -------------------- EQUIPMENT ENDPOINTS --------------------
@router.post("/equipments", response_model=EquipmentResponseSchema)
def create_equipment_api(equipment_data: CreateEquipmentSchema, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return create_equipment(db, equipment_data)

@router.post("/rooms/{room_id}/equipment/{equipment_id}/assign")
def assign_equipment(room_id: int, equipment_id: int, quantity: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return assign_equipment_to_room(db, room_id, equipment_id, quantity)

@router.post("/rooms/{room_id}/equipment/{equipment_id}/unassign")
def unassign_equipment(room_id: int, equipment_id: int, quantity: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return unassign_equipment_from_room(db, room_id, equipment_id, quantity)

@router.get("/search-equipments", response_model=List[EquipmentResponseSchema])
def search_equipment_by_keyword(
    keyword: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return search_equipments_by_keyword(db, keyword)

@router.get("/equipments", response_model=List[EquipmentResponseSchema])
def get_all_hospital_equipments(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return get_all_equipments(db)

@router.get("/equipment/{equipment_id}", response_model=EquipmentResponseSchema)
def get_equipment_by_its_id(
    equipment_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return get_equipment_by_id(equipment_id, db)
# -------------------- PATIENT ENDPOINTS --------------------
@router.get("/patients", response_model=List[PatientResponseSchema])
def list_all_patients(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_all_patients(db)

@router.get("/patients/today", response_model=List[PatientResponseSchema])
def list_today_patients(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_today_patients(db)

@router.get("/patients/search", response_model=List[PatientResponseSchema])
def search_patients_route(
    query: str = Query(...),
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return search_patients(db=db, keyword=query)
# -------------------- STATISTICS ENDPOINT --------------------
@router.get("/statistics")
def get_patient_stats(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_patient_statistics(db)

@router.get("/patients/{patient_id}", response_model=PatientResponseSchema)
def get_patient(patient_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient



# -------------------- DOCTOR ENDPOINTS --------------------
@router.get("/doctors", response_model=List[DoctorResponseSchema])
def list_all_doctors(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_all_doctors(db)

@router.get("/doctors/available", response_model=List[DoctorResponseSchema])
def list_available_doctors(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_available_doctors(db)


@router.get("/search-doctors", response_model=List[DoctorResponseSchema])
def search_doctors(
    keyword: str = Query(..., description="Search keyword"),
    db: Session = Depends(get_db),
):
    keyword_filter = f"%{keyword.lower()}%"

    query = db.query(Doctor).filter(
        (Doctor.user.has(User.firstname.ilike(keyword_filter))) |
        (Doctor.user.has(User.lastname.ilike(keyword_filter))) |
        (Doctor.user.has(User.username.ilike(keyword_filter))) |
        (Doctor.specialization.ilike(keyword_filter)) |
        (Doctor.department.ilike(keyword_filter))
    )

    return query.all()


@router.get("/doctors/{doctor_id}", response_model=DoctorResponseSchema)
def get_doctor(doctor_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    doctor = get_doctor_by_id(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
# -------------------- NURSE ENDPOINTS --------------------
@router.get("/nurses", response_model=List[NurseResponseSchema])
def list_all_nurses(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_all_nurses(db)

@router.get("/nurses/available", response_model=List[NurseResponseSchema])
def list_available_nurses(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_available_nurses(db)

@router.get("/nurses/{nurse_id}", response_model=NurseResponseSchema)
def get_nurse(nurse_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_nurse_by_id(db, nurse_id)

@router.get("/search-nurses", response_model=List[NurseResponseSchema])
def search_nurses(
    keyword: str = Query(..., description="Search keyword"),
    db: Session = Depends(get_db),
):
    keyword_filter = f"%{keyword.lower()}%"

    query = db.query(Nurse).filter(
        (Nurse.user.has(User.firstname.ilike(keyword_filter))) |
        (Nurse.user.has(User.lastname.ilike(keyword_filter))) |
        (Nurse.user.has(User.username.ilike(keyword_filter))) |
        (Nurse.department.ilike(keyword_filter))
    )

    return query.all()

# -------------------- RECEPTIONIST ENDPOINTS --------------------
@router.get("/receptionists", response_model=List[ReceptionistResponseSchema])
def list_all_receptionists(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_all_receptionists(db)

@router.get("/receptionists/{receptionist_id}", response_model=ReceptionistResponseSchema)
def get_receptionist(receptionist_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_receptionist_by_id(db, receptionist_id)

@router.get("/search-recep", response_model=List[ReceptionistResponseSchema])
def search_recep(
    keyword: str = Query(..., description="Search keyword"),
    db: Session = Depends(get_db),
):
    keyword_filter = f"%{keyword.lower()}%"

    query = db.query(Receptionist).filter(
        (Receptionist.user.has(User.firstname.ilike(keyword_filter))) |
        (Receptionist.user.has(User.lastname.ilike(keyword_filter))) |
        (Receptionist.user.has(User.username.ilike(keyword_filter))) |
        (Receptionist.languages_spoken.ilike(keyword_filter))
    )

    return query.all()

# -------------------- ROOM ENDPOINTS --------------------
@router.post("/rooms", response_model=RoomResponseSchema)
def add_room(room_data: CreateRoomSchema, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return create_room(db, room_data)

@router.get("/rooms/available", response_model=List[RoomResponseSchema])
def get_available_room_list(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return get_available_rooms(db)

