from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4

class Note(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default='no description provided yet', max_length=1000)
    
class CreateNote(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default='no description provided yet', max_length=1000)
    
class UpdateNote(BaseModel):
    title: Optional[str] = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default='no description provided yet', max_length=1000)
    