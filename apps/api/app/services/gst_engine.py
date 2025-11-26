from decimal import Decimal
from typing import Dict, Optional
from pydantic import BaseModel

class TaxComponents(BaseModel):
    cgst: Decimal = Decimal("0.0")
    sgst: Decimal = Decimal("0.0")
    igst: Decimal = Decimal("0.0")
    cess: Decimal = Decimal("0.0")
    total_tax: Decimal = Decimal("0.0")

def calculate_tax(
    taxable_value: Decimal,
    rate: Decimal,
    is_interstate: bool,
    cess_rate: Decimal = Decimal("0.0")
) -> TaxComponents:
    """
    Calculate GST components based on taxable value and rate.
    
    Args:
        taxable_value: The value on which tax is calculated.
        rate: The GST rate (e.g., 5, 12, 18, 28).
        is_interstate: True if supply is interstate (IGST), False otherwise (CGST+SGST).
        cess_rate: Compensation cess rate if applicable.
        
    Returns:
        TaxComponents object with calculated values.
    """
    tax_amount = (taxable_value * rate) / Decimal("100.0")
    cess_amount = (taxable_value * cess_rate) / Decimal("100.0")
    
    components = TaxComponents(cess=cess_amount)
    
    if is_interstate:
        components.igst = tax_amount
    else:
        # Divide equally between CGST and SGST
        half_tax = tax_amount / Decimal("2.0")
        components.cgst = half_tax
        components.sgst = half_tax
        
    components.total_tax = components.cgst + components.sgst + components.igst + components.cess
    return components

def determine_place_of_supply(
    supplier_state_code: str,
    recipient_state_code: str
) -> str:
    """
    Determine if the supply is Interstate or Intrastate.
    
    Args:
        supplier_state_code: 2-digit state code of supplier.
        recipient_state_code: 2-digit state code of recipient.
        
    Returns:
        'INTER' if states are different, 'INTRA' if same.
    """
    if supplier_state_code == recipient_state_code:
        return "INTRA"
    return "INTER"
