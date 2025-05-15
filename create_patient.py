from datetime import date
from app.core.database import SessionLocal
from app.models.patient import Patient

db = SessionLocal()

patient = Patient(
    firstname="Aya",
    lastname="Smith",
    gender="Female",
    date_of_birth=date(1990, 1, 1),  # date object, not string
    medicalHistory="None",          # make sure these names match your model
    currentStatus="admitted",
    admission_date=date.today(),
    room_id=None,
    discharge_date=None,
    emergency_contact="John Smith - 123456789",
    insurance_provider="HealthCare Inc."
)

db.add(patient)
db.commit()
db.refresh(patient)
print(f"Patient created: ID={patient.patientID}, Name={patient.firstname} {patient.lastname}")

db.close()

