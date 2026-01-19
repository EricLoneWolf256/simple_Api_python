from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# temporary in-memory storage for notes
notes = {}
class Note(BaseModel):
    title: str
    content: str
    
@app.post("/notes/")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note created successfully", "note": note}

@app.get("/notes/")
def get_notes():
    return {"notes": notes}