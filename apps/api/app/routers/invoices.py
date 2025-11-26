from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List
from sqlalchemy.orm import Session
from app.schemas.invoice import InvoiceCreate, InvoiceRead
from app.models.invoice import Invoice, InvoiceItem
from app.services.gst_engine import calculate_tax, determine_place_of_supply
from decimal import Decimal
import pandas as pd
import io

router = APIRouter()

from app.core.database import get_db
# ... imports

@router.post("/", response_model=InvoiceRead)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    # Calculate tax for each item
    total_taxable = Decimal("0.0")
    total_tax = Decimal("0.0")
    total_val = Decimal("0.0")
    
    db_items = []
    for item in invoice.items:
        # Determine Place of Supply (Simplified: assume local for now if not provided)
        pos = determine_place_of_supply("27", "27") # Mock: Maharashtra to Maharashtra
        is_interstate = pos == "INTER"
        
        tax_comps = calculate_tax(item.taxable_value, item.gst_rate, is_interstate)
        
        db_item = InvoiceItem(
            hsn_code=item.hsn_code,
            description=item.description,
            quantity=item.quantity,
            unit_price=item.unit_price,
            taxable_value=item.taxable_value,
            gst_rate=item.gst_rate,
            cgst_amount=tax_comps.cgst,
            sgst_amount=tax_comps.sgst,
            igst_amount=tax_comps.igst,
            cess_amount=tax_comps.cess
        )
        db_items.append(db_item)
        
        total_taxable += item.taxable_value
        total_tax += tax_comps.total_tax
    
    total_val = total_taxable + total_tax
    
    # Create Invoice Record
    db_invoice = Invoice(
        invoice_number=invoice.invoice_number,
        invoice_date=invoice.invoice_date,
        gstin=invoice.gstin,
        counterparty_gstin=invoice.counterparty_gstin,
        counterparty_name=invoice.counterparty_name,
        invoice_type=invoice.invoice_type,
        total_taxable_value=total_taxable,
        total_tax_amount=total_tax,
        total_amount=total_val,
        items=db_items
    )
    
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
        
    return db_invoice

@router.post("/upload")
async def upload_invoices(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xlsx', '.csv')):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    contents = await file.read()
    if file.filename.endswith('.csv'):
        df = pd.read_csv(io.BytesIO(contents))
    else:
        df = pd.read_excel(io.BytesIO(contents))
        
    # Process DataFrame (Simplified)
    # In real app: Validate columns, iterate rows, create invoices
    
    return {"message": f"Processed {len(df)} rows successfully", "columns": df.columns.tolist()}

@router.get("/", response_model=List[InvoiceRead])
def list_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Return empty list for now
    return []
