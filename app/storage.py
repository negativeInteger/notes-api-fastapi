import json
from typing import List
from app.models import Note
from pathlib import Path

# define path to the JSON file
DATA_FILE = Path('notes.json')

# ensure that JSON file exists
if not DATA_FILE.exists():
    DATA_FILE.write_text('[]')
    
# read notes
def read_notes() -> List[Note]:
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        # convert dicts to Note objects
        return [Note(**item) for item in data]

# write notes
def write_notes(notes: List[Note]) -> None:
    with open(DATA_FILE, 'w') as file:
        # convert Note objects to dicts before saving
        json.dump([note.model_dump() for note in notes], file, indent=4)