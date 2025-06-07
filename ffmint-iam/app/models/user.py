"""SQLAlchemy User model and slug generator."""

import uuid
from datetime import datetime

from slugify import slugify
from sqlalchemy import Boolean, DateTime, String, Text, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy declarative models."""

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} instance>"

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the SQLAlchemy model instance,
        including all mapped columns and their values.
        """
        return {
            column.key: getattr(self, column.key) for column in self.__mapper__.columns
        }


class User(Base):
    """User database model."""

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    first_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    country: Mapped[str | None] = mapped_column(String(2), nullable=True)
    profile_pic: Mapped[str | None] = mapped_column(Text, nullable=True)
    contact_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    slug: Mapped[str | None] = mapped_column(String(100), nullable=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime, default=None, onupdate=datetime.utcnow
    )

    def full_name(self) -> str:
        """Return the user's full name, handling optional first name."""
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.last_name

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, slug={self.slug})>"


@event.listens_for(User, "before_insert")
def generate_slug(_mapper, _connect, target: User) -> None:
    """
    Auto-generate a slug before inserting a user.

    Parameters
    ----------
    _mapper : Mapper
        SQLAlchemy mapper (unused).
    _connect : Connection
        DB connection (unused).
    target : User
        User instance being inserted.
    """
    if not target.slug:
        base = f"{target.first_name or ''}-{target.last_name}"
        target.slug = slugify(base)
