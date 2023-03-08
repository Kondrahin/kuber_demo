"""Repo dependencies."""

from fastapi import Depends

from app.db.crud.events.repo import EventRepo
from app.settings.config import get_app_settings

config = get_app_settings()

get_event_repo_dependency = Depends(EventRepo)
