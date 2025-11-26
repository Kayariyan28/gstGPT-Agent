from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.returns import GSTR1Summary, GSTR3BSummary
from app.services.returns_service import generate_gstr1_data, generate_gstr3b_data

router = APIRouter()

def get_db():
    yield None

@router.get("/gstr1", response_model=GSTR1Summary)
def get_gstr1(gstin: str, period: str, db: Session = Depends(get_db)):
    return generate_gstr1_data(db, gstin, period)

@router.get("/gstr3b", response_model=GSTR3BSummary)
def get_gstr3b(gstin: str, period: str, db: Session = Depends(get_db)):
    return generate_gstr3b_data(db, gstin, period)
