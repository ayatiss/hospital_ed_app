from app.core.database import SessionLocal
from app.models.room import Room

db = SessionLocal()

room = Room(
    name="ICU Room 101",
    type="ICU",
    status="available",
    capacity=1,
    floor=1,
    wing="A"
)

db.add(room)
db.commit()
db.refresh(room)
print(f"Room created: ID={room.room_id}, Name={room.name}")
db.close()
