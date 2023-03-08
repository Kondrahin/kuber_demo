"""Event repo."""
import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import NoResultFound

from app.db.models import Event
from app.schemas.event import CreateEventSchema, EventSchema


class EventRepo:
    async def create_event(
        self, event_to_create: CreateEventSchema
    ) -> uuid.UUID:
        event_uuid = uuid.uuid4()
        await Event.create(
            **event_to_create.dict(),
            uuid=event_uuid,
            created_datetime=datetime.now(),
        )
        return event_uuid

    async def get_event(self, event_uuid: UUID) -> Optional[EventSchema]:
        try:
            event = await Event.get(uuid=event_uuid)
        except NoResultFound:
            return None

        return EventSchema.from_orm(event)

    async def get_all_event(self) -> Optional[List[EventSchema]]:
        try:
            events = await Event.all()
        except NoResultFound:
            return None

        events = [EventSchema.from_orm(event) for event in events]
        return sorted(events, key=lambda event: event.event_datetime, reverse=True)
