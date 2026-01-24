from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

import models
import schemas
from database import engine, get_db
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ---------- AUTH ----------

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.username == form_data.username
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/protected")
def protected(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authenticated"}


# ---------- NOTES ----------

@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = models.Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@app.get("/notes", response_model=list[schemas.NoteResponse])
def get_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Note).offset(skip).limit(limit).all()


@app.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    for key, value in note.model_dump(exclude_unset=True).items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note)
    return db_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
