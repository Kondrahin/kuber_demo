"""Event schema."""
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from pydantic import BaseModel


class CreateEventSchema(BaseModel):
    title: str
    description: Optional[str]
    location: str
    scope: Any
    event_datetime: datetime


class EventSchema(BaseModel):
    uuid: UUID
    title: str
    description: Optional[str]
    location: str
    scope: Any
    event_datetime: datetime

    class Config:
        orm_mode = True
