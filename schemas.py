from pydantic import BaseModel, Field
from typing import Optional

# ---------- NOTES ----------

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(NoteBase):
    id: int

    class Config:
        from_attributes = True


# ---------- USERS ----------

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=6, max_length=72)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
