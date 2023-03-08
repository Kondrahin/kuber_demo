"""Entity dependencies."""
from uuid import UUID

from fastapi import Depends, HTTPException
from starlette import status

from app.api.v1.dependencies.google_authentication import get_token_data_dependency
from app.api.v1.dependencies.repo import (
    get_comment_repo_dependency,
    get_event_repo_dependency,
    get_moderator_repo_dependency,
)
from app.db.crud.events.repo import EventRepo
from app.resources import strings
from app.schemas.event import EventSchema
from app.settings.config import get_app_settings

config = get_app_settings()


async def get_event(
    event_uuid: UUID,
    event_repo: EventRepo = get_event_repo_dependency,
) -> EventSchema:
    event = await event_repo.get_event(event_uuid)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.EVENT_NOT_FOUND_ERROR,
        )

    return event


get_event_dependency = Depends(get_event)
