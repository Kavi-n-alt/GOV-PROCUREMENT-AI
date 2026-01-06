from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.tender import TenderOut, TenderCreate
from app.db.session import get_db
from app.models.tender import Tender as TenderModel

router = APIRouter()


@router.get("/tenders", response_model=List[TenderOut])
async def list_tenders(limit: int = 50, db: Session = Depends(get_db)):
    """Return a list of tenders from DB."""
    items = db.query(TenderModel).order_by(TenderModel.created_at.desc()).limit(limit).all()
    return items


@router.get("/tenders/{tender_id}", response_model=TenderOut)
async def get_tender(tender_id: int, db: Session = Depends(get_db)):
    obj = db.query(TenderModel).filter(TenderModel.id == tender_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Tender not found")
    return obj


@router.post("/tenders", response_model=TenderOut)
async def create_tender(payload: TenderCreate, db: Session = Depends(get_db)):
    obj = TenderModel(title=payload.title, description=payload.description or "", source=payload.source or "")
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
