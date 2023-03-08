"""Functions to create and close connections to db."""
from typing import Optional

from starlette.datastructures import URL

from app.db.redis.repo import RedisRepo
from app.db.sqlalchemy import session_fabric


async def init_db() -> None:
    """Create connection to db and init orm models."""
    await session_fabric.init()


async def close_db() -> None:
    """Close connection to db."""
    await session_fabric.close()
