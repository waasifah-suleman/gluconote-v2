from datetime import date, datetime

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

class GeneralNote(Base):
    """A free-form note logged by a user to record observations, side effects, or other context"""

    __tablename__ = "general_notes"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    note: str = Column(String, nullable=False)

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())