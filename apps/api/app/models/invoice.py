from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

# Base is now imported from database.py

class InvoiceType(str, enum.Enum):
    B2B = "B2B"
    B2C = "B2C"
    EXPORT = "EXPORT"

class InvoiceStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    UPLOADED = "UPLOADED"
    FILED = "FILED"

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, index=True)
    invoice_date = Column(Date)
    gstin = Column(String, index=True) # Supplier GSTIN for Purchase, My GSTIN for Sales
    counterparty_gstin = Column(String, nullable=True)
    counterparty_name = Column(String, nullable=True)
    invoice_type = Column(String, default=InvoiceType.B2B)
    status = Column(String, default=InvoiceStatus.DRAFT)
    
    total_taxable_value = Column(Numeric(12, 2))
    total_tax_amount = Column(Numeric(12, 2))
    total_amount = Column(Numeric(12, 2))
    
    items = relationship("InvoiceItem", back_populates="invoice")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    
    hsn_code = Column(String)
    description = Column(String, nullable=True)
    quantity = Column(Numeric(10, 2), default=0)
    unit_price = Column(Numeric(10, 2), default=0)
    
    taxable_value = Column(Numeric(12, 2))
    gst_rate = Column(Numeric(5, 2)) # 5, 12, 18, 28
    
    cgst_amount = Column(Numeric(12, 2), default=0)
    sgst_amount = Column(Numeric(12, 2), default=0)
    igst_amount = Column(Numeric(12, 2), default=0)
    cess_amount = Column(Numeric(12, 2), default=0)
    
    invoice = relationship("Invoice", back_populates="items")
