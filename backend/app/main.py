"""Application with configuration for events, routers and middleware."""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.api.v1.routers import api_router
from app.db.error_handlers.db import db_not_raise_up_handler
from app.settings.config import get_app_settings
from app.settings.events import shutdown, startup

config = get_app_settings()


def get_application() -> FastAPI:
    """Create configured server application instance."""
    application = FastAPI(title="punk-events", docs_url="/api/v1/docs")

    application.add_event_handler(
        "startup",
        startup(),
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    application.add_event_handler("shutdown", shutdown())

    application.add_exception_handler(OSError, db_not_raise_up_handler)
    application.include_router(api_router)

    return application


app = get_application()
