from datetime import date, datetime

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

class DoctorVisit(Base):
    """A record of a user's visit to a doctor, with optional clinic and notes"""

    __tablename__ = "doctor_visits"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    visit_date: date = Column(Date, nullable=False)
    doctor_name: str = Column(String, nullable=False)
    clinic_name: str | None = Column(String, nullable=True)
    notes: str | None = Column(String, nullable=True)

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())

