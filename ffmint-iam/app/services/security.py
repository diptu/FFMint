"""
Security utilities for password hashing and verification.

This module provides functions to securely hash passwords using bcrypt
and verify plain-text passwords against hashed versions using Passlib.
Security service with DB session dependency
"""

from typing import Generator

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db() -> Generator[Session, None, None]:
    """
    Yield a new database session.

    Yields
    -------
    Session
        SQLAlchemy session object.
    """
    data_base: Session = SessionLocal()
    try:
        yield data_base
    finally:
        data_base.close()


def get_password_hash(password: str) -> str:
    """
    Hash a plain text password.

    Parameters
    ----------
    password : str
        Plain password to hash.

    Returns
    -------
    str
        Bcrypt-hashed password string.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.

    Parameters
    ----------
    plain_password : str
        User input password (not hashed).
    hashed_password : str
        Stored hashed password.

    Returns
    -------
    bool
        True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
