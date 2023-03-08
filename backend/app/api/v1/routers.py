"""Configuration of routers for all endpoints."""
from fastapi import APIRouter

from app.api.v1.endpoints import event

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(event.router, prefix="/events", tags=["events"])
