from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import sessionlocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class NoteCreate(BaseModel):
    title: str
    content: str
    
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/notes/")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
@app.get("/notes/")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

# notes = []
# class Note(BaseModel):
#     title: str
#     content: str

# @app.post("/notes/")
# def create_note(note: Note):
#     notes.append(note)
#     return {"message": "Note created", "note": note}

# @app.get("/notes/")
# def get_notes():
#     return notes

# @app.put("/notes/{note_id}")
# def update_note(note_id: int, updated_note: Note):
#     if note_id < 0 or note_id >= len(notes):
#         raise HTTPException(status_code=404, detail="Note not found")
#     notes[note_id] = updated_note
#     return {"message": "Note updated", "note": updated_note}

# @app.delete("/notes/{note_id}")
# def delete_note(note_id: int):
#     if note_id < 0 or note_id >= len(notes):
#         raise HTTPException(status_code=404, detail="Note not found")
#     deleted_note = notes.pop(note_id)
#     return {"message": "Note deleted", "note": deleted_note}