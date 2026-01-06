from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from starlette.status import HTTP_202_ACCEPTED
from sqlalchemy.orm import Session

from app.services import extractor, normalizer
from app.db.session import get_db
from app.models.tender import Tender as TenderModel

router = APIRouter()


@router.post("/upload", status_code=HTTP_202_ACCEPTED)
async def upload_tender(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Accept a PDF (or other) and start processing pipeline."""
    if file.content_type not in ("application/pdf", "application/octet-stream"):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # extract (stub)
    raw = await extractor.extract_from_uploadfile(file)
    # normalize (stub)
    tender = normalizer.normalize(raw)

    # persist a tender record (simple sync DB write)
    obj = TenderModel(
        title=tender.get("title") or file.filename,
        description=tender.get("description"),
        raw_text=tender.get("raw", {}).get("raw_text"),
        source=f"upload:{file.filename}",
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return {"message": "file received", "tender_id": obj.id, "tender_preview": {"title": obj.title}}
