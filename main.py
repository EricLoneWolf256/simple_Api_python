from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

notes = []
class Note(BaseModel):
    title: str
    content: str

@app.post("/notes/")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note created", "note": note}

@app.get("/notes/")
def get_notes():
    return notes

@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    notes[note_id] = updated_note
    return {"message": "Note updated", "note": updated_note}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    deleted_note = notes.pop(note_id)
    return {"message": "Note deleted", "note": deleted_note}