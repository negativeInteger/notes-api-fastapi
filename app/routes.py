from fastapi import APIRouter, HTTPException, status, Response
from app.models import Note, CreateNote, UpdateNote
from app.storage import read_notes, write_notes

# create a router instance
router = APIRouter()

# Get all notes
@router.get('/notes', response_model=list[Note])
def get_notes():
    return read_notes()

# Create a new note
@router.post('/notes', response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note: CreateNote):
    notes = read_notes()
    
    new_note = Note(
        title = note.title,
        description = note.description
    )
    
    notes.append(new_note)
    write_notes(notes)
    return new_note

# Get note by ID
@router.get('/notes/{note_id}', response_model=Note)
def get_note(note_id: str):
    notes = read_notes()
    
    for note in notes:
        if note.id == note_id:
            return note
        
    raise HTTPException(
        status_code=404,
        detail='no note with this ID'
    )

# Update note by ID
@router.put('/notes/{note_id}', response_model=Note)
def update_note(note_id: str, updated_note: UpdateNote):
    notes = read_notes()
    
    if not updated_note.title and not updated_note.description:
        raise HTTPException(
            status_code=400,
            detail='At least one property must be updated'
        )
    
    for note in notes:
        if note.id == note_id:
            if updated_note.title:
                note.title = updated_note.title
            if updated_note.description:
                note.description = updated_note.description
            write_notes(notes)
            return note
    
    raise HTTPException(
        status_code=404,
        detail='no note with this ID'
    )
    
# Delete note by ID
@router.delete('/notes/{note_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: str):
    notes = read_notes()
    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            write_notes(notes)
            return         
    raise HTTPException(status_code=404, detail="Note not found")
    
    
    
