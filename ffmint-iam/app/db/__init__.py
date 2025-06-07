"""Database session dependency."""

from typing import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal  # Your SQLAlchemy session factory


def get_db() -> Generator[Session, None, None]:
    """
    Yield a SQLAlchemy Session instance.

    This function provides a database session to dependencies and
    ensures proper cleanup after use.

    Yields
    ------
    Session
        A SQLAlchemy Session instance.
    """
    db_session: Session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
