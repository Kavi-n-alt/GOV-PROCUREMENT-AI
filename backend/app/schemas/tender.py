from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TenderOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    source: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class TenderCreate(BaseModel):
    title: str
    description: Optional[str]
    source: Optional[str]
