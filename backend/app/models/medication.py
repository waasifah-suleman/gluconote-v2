from datetime import date, datetime

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

class Medication(Base):
    """A medication prescribed to a user, with an optional end date for ongoing prescriptions."""

    __tablename__ = "medications"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    name: str = Column(String, nullable=False)
    dosage: str = Column(String, nullable=False)

    start_date: date = Column(Date, nullable=False)
    # left blank if medication is still ongoing
    end_date: date | None = Column(Date, nullable=True)

    prescribing_doctor: str = Column(String, nullable=False)

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())