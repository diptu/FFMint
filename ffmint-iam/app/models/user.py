import re
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, String, event
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Mapped, Mapper, mapped_column

from app.db.base import Base


def slugify(value: str) -> str:
    value = re.sub(r"[\s_]+", "-", value.lower())
    return re.sub(r"[^a-z0-9-]", "", value)


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        pgUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )

    first_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(
        String, unique=True, index=True, nullable=True
    )

    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    country: Mapped[Optional[str]] = mapped_column(String(length=2), nullable=True)
    profile_pic: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    contact_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=datetime.now
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=datetime.now
    )


@event.listens_for(User, "before_insert")
def generate_slug(
    mapper: Mapper,
    connection: Connection,
    target: User,
) -> None:
    if not target.slug and target.last_name:
        target.slug = slugify(target.last_name)
