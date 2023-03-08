import pytest
from pydantic import ValidationError

from app.settings.environments.test import AppSettings


def test_credentials_validation():
    AppSettings(
        DEBUG=True,
        SQL_DEBUG=True,
        POSTGRES_DSN="postgres://postgres:postgres@localhost/postgres",
    )
    with pytest.raises(ValidationError):
        AppSettings(
            DEBUG=True,
            SQL_DEBUG=True,
        )
