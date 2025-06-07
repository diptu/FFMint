"""Test for DB session dependency."""

from typing import Generator

import pytest
from sqlalchemy.orm import Session

from app.services.security import get_db


def test_get_db_yields_session() -> None:
    """
    Ensure get_db yields a SQLAlchemy Session.
    """
    db_gen: Generator[Session, None, None] = get_db()
    session = next(db_gen)

    assert isinstance(session, Session), "Did not yield a SQLAlchemy session"

    # Ensure generator is exhausted after yielding once
    with pytest.raises(StopIteration):
        next(db_gen)
