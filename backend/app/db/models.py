"""Database models declarations."""

from datetime import datetime
from typing import Any, Generic, List, TypeVar
from uuid import UUID

import sqlalchemy as sa
from pydantic import EmailStr
from sqlalchemy.dialects import postgresql
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from app.db.sqlalchemy import Base, session_fabric

T = TypeVar("T")  # noqa: WPS111


class CRUDMixin(Generic[T]):
    """Mixin for CRUD operations for models."""

    id: int

    @classmethod
    async def create(cls, **kwargs: Any) -> None:
        """Create object."""
        session = session_fabric.get_session()
        query = sa.insert(cls).values(**kwargs)
        async with session.begin():
            await session.execute(query)

    @classmethod
    async def get(cls, **kwargs: Any) -> T:
        """Get object by kwargs."""
        session = session_fabric.get_session()
        query = select(cls).filter_by(**kwargs)
        async with session.begin():
            rows = await session.execute(query)
        return rows.scalars().unique().one()

    @classmethod
    async def all(cls, **kwargs: Any) -> List[T]:
        """Get all objects."""
        session = session_fabric.get_session()
        query = select(cls).filter_by(**kwargs)
        async with session.begin():
            rows = await session.execute(query)
        return rows.scalars().unique().all()


class Event(Base, CRUDMixin):
    """Event database model."""

    __tablename__ = "event"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    uuid: UUID = sa.Column(postgresql.UUID(as_uuid=True), nullable=False, unique=True)
    title: str = sa.Column(sa.String, nullable=False)
    description: str = sa.Column(sa.String, nullable=True)
    location: str = sa.Column(sa.String, nullable=False)
    scope: str = sa.Column(sa.String, nullable=False)
    created_datetime: datetime = sa.Column(sa.DateTime(timezone=True), nullable=False)
    event_datetime: datetime = sa.Column(sa.DateTime(timezone=True), nullable=False)
