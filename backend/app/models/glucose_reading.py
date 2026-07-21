import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, Float, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

class ReadingContextEnum(str, enum.Enum):
    FASTING = "fasting"
    BEFORE_MEAL = "before_meal"
    AFTER_MEAL = "after_meal"
    BEDTIME = "bedtime"
    RANDOM = "random"
    OTHER = "other"

class GlucoseReading(Base):
    """A single blood glucose measurement logged by a user."""

    __tablename__ = "glucose_readings"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Store in mmol/L, matching the user's target range units
    value: float = Column(Float, nullable=False)

    # Auto-recorded on creation, but editable by the user afterward
    recorded_at: datetime = Column(DateTime(timezone=True), server_default=func.now())

    context: ReadingContextEnum | None = Column(Enum(ReadingContextEnum), nullable=True)

    note: str | None = Column(String(50), nullable=True)

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())