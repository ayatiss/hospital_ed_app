from app.core.database import SessionLocal
from app.models.equipement import Equipment

db = SessionLocal()

equipment = Equipment(
    name="Ventilator",
    type="life-support",
    status="available",
    total_quantity=10,
    available_quantity=10,
    location="ICU Storage",
    last_maintenance_date="2025-04-01",
    manufacturer="MedEquip Inc.",
    purchase_date="2023-11-20"
)

db.add(equipment)
db.commit()
db.refresh(equipment)
print(f"Equipment created: ID={equipment.equipmentID}, Name={equipment.name}")
db.close()
