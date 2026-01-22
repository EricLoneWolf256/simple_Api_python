from pydantic import BaseModel
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int

    class Config:
        from_attributes = True
        
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
