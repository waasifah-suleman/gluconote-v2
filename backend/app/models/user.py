import enum
from datetime import date, datetime

from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Float
from sqlalchemy.sql import func

from app.core.database import Base

class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class DiabetesTypeEnum(str, enum.Enum):
    """Fixed set of diabetes diagnoses supported by the app."""

    TYPE_1 = "type_1"
    TYPE_2 = "type_2"
    GESTATIONAL = "gestational"
    PREDIABETES = "prediabetes"
    OTHER = "other"

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)

    # Auth fields
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    phone: str | None = Column(String, nullable=True)

    # Profile fields
    name: str = Column(String, nullable=False)
    gender: GenderEnum | None = Column(Enum(GenderEnum), nullable=True)
    date_of_birth: date = Column(Date, nullable=False)
    diabetes_type: DiabetesTypeEnum = Column(Enum(DiabetesTypeEnum), nullable=False)

    # Target range stored in mmol/L
    target_range_low: float = Column(Float, nullable=False)
    target_range_high: float = Column(Float, nullable=False)

    height_cm: float | None = Column(Float, nullable=True)
    weight_kg: float | None = Column(Float, nullable=True)

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())