from fastapi import UploadFile
from typing import Dict


async def extract_from_uploadfile(file: UploadFile) -> Dict:
    """Stub: read file bytes and return raw text / metadata dict.
    Replace with a real PDF extractor (pdfminer, pypdf, or your existing extractor module).
    """
    content = await file.read()
    # naive fallback - return raw text blob placeholder
    return {"raw_text": content.decode(errors="ignore"), "filename": file.filename}
