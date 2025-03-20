from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class Note(BaseModel):
    id: UUID
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    