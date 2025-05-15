from app.core.database import SessionLocal
from app.models.admin import Admin
from app.services.auth import hash_password

db = SessionLocal()

hashed = hash_password("admin123")
print("Hashed password:", hashed)

admin = Admin(
    username="adminuser",
    firstname="Admin",
    lastname="Test",
    role="admin",
    number="1234567890",
    email="admin@example.com",
    hashed_password=hashed,
    address="sfax",
    gender="male",
    date_of_birth="1992-03-15",
    hire_date="2022-03-15",
    is_archived=False,
    is_available=True
)

db.add(admin)
db.commit()
db.refresh(admin)
print(f"Admin created: {admin.userID}")
db.close()

