from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

# --- GSTR-1 Schemas ---

class B2BItem(BaseModel):
    ctin: str  # Counterparty GSTIN
    inv_no: str
    inv_dt: str
    val: Decimal
    pos: str
    rchrg: str = "N"
    inv_typ: str = "R"
    tax_val: Decimal
    rt: Decimal
    iamt: Decimal = Decimal("0.0")
    camt: Decimal = Decimal("0.0")
    samt: Decimal = Decimal("0.0")
    csamt: Decimal = Decimal("0.0")

class GSTR1Summary(BaseModel):
    gstin: str
    fp: str  # Financial Period e.g. 082025
    b2b: List[B2BItem] = []
    # Add other sections like b2cl, b2cs, exp, etc. as needed

# --- GSTR-3B Schemas ---

class GSTR3BTable31(BaseModel):
    # 3.1 Details of Outward Supplies and inward supplies liable to reverse charge
    txval: Decimal = Decimal("0.0")
    iamt: Decimal = Decimal("0.0")
    camt: Decimal = Decimal("0.0")
    samt: Decimal = Decimal("0.0")
    csamt: Decimal = Decimal("0.0")

class GSTR3BTable4(BaseModel):
    # 4. Eligible ITC
    iamt: Decimal = Decimal("0.0")
    camt: Decimal = Decimal("0.0")
    samt: Decimal = Decimal("0.0")
    csamt: Decimal = Decimal("0.0")

class GSTR3BSummary(BaseModel):
    gstin: str
    fp: str
    sup_details: GSTR3BTable31  # 3.1(a) Outward taxable supplies
    itc_elg: GSTR3BTable4       # 4(A) ITC Available (All other ITC)
