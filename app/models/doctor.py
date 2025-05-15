from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.user import User
from sqlalchemy.orm import relationship

class Doctor(User):
    __tablename__ = "doctors"

    doctorID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    department = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    specialization = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    years_of_experience = Column(String, nullable=True)

    # ✅ Add relationship to user
    user = relationship("User", backref="doctor", uselist=False)

    __mapper_args__ = {
        "polymorphic_identity": "doctor",
    }
