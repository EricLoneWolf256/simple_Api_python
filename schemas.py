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


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True