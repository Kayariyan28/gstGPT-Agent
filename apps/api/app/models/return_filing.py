from sqlalchemy import Column, Integer, String, Date, Enum, DateTime
from sqlalchemy.sql import func
from app.models.invoice import Base
import enum

class ReturnType(str, enum.Enum):
    GSTR1 = "GSTR1"
    GSTR3B = "GSTR3B"

class ReturnStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    FILED = "FILED"
    ERROR = "ERROR"

class ReturnFiling(Base):
    __tablename__ = "return_filings"

    id = Column(Integer, primary_key=True, index=True)
    gstin = Column(String, index=True)
    period = Column(String, index=True) # MMYYYY
    return_type = Column(String, default=ReturnType.GSTR1)
    status = Column(String, default=ReturnStatus.DRAFT)
    
    ack_number = Column(String, nullable=True)
    filed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
