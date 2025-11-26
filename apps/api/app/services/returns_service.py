from sqlalchemy.orm import Session
from app.models.invoice import Invoice, InvoiceType
from app.schemas.returns import GSTR1Summary, B2BItem, GSTR3BSummary, GSTR3BTable31, GSTR3BTable4
from decimal import Decimal
from typing import List

def generate_gstr1_data(db: Session, gstin: str, period: str) -> GSTR1Summary:
    # Mock implementation: In real app, query DB filtering by date range derived from period
    # Period format: MMYYYY e.g. 082025
    
    # Fetch B2B Invoices
    # invoices = db.query(Invoice).filter(...).all()
    
    # Mock Data
    b2b_items = [
        B2BItem(
            ctin="27ABCDE1234F1Z5",
            inv_no="INV-001",
            inv_dt="01-08-2025",
            val=Decimal("1180.00"),
            pos="27",
            tax_val=Decimal("1000.00"),
            rt=Decimal("18.0"),
            camt=Decimal("90.0"),
            samt=Decimal("90.0")
        )
    ]
    
    return GSTR1Summary(
        gstin=gstin,
        fp=period,
        b2b=b2b_items
    )

def generate_gstr3b_data(db: Session, gstin: str, period: str) -> GSTR3BSummary:
    # Mock implementation
    
    # 3.1(a) Outward Taxable Supplies
    sup_details = GSTR3BTable31(
        txval=Decimal("10000.00"),
        iamt=Decimal("0.0"),
        camt=Decimal("900.0"),
        samt=Decimal("900.0"),
        csamt=Decimal("0.0")
    )
    
    # 4(A)(5) All other ITC
    itc_elg = GSTR3BTable4(
        iamt=Decimal("500.0"),
        camt=Decimal("250.0"),
        samt=Decimal("250.0"),
        csamt=Decimal("0.0")
    )
    
    return GSTR3BSummary(
        gstin=gstin,
        fp=period,
        sup_details=sup_details,
        itc_elg=itc_elg
    )
