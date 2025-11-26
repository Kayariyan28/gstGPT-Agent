from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from decimal import Decimal

class InvoiceItemBase(BaseModel):
    hsn_code: str
    description: Optional[str] = None
    quantity: Decimal
    unit_price: Decimal
    taxable_value: Decimal
    gst_rate: Decimal

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItemRead(InvoiceItemBase):
    id: int
    cgst_amount: Decimal
    sgst_amount: Decimal
    igst_amount: Decimal
    cess_amount: Decimal

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    invoice_number: str
    invoice_date: date
    gstin: str
    counterparty_gstin: Optional[str] = None
    counterparty_name: Optional[str] = None
    invoice_type: str = "B2B"

class InvoiceCreate(InvoiceBase):
    items: List[InvoiceItemCreate]

class InvoiceRead(InvoiceBase):
    id: int
    status: str
    total_taxable_value: Decimal
    total_tax_amount: Decimal
    total_amount: Decimal
    items: List[InvoiceItemRead]

    class Config:
        from_attributes = True
