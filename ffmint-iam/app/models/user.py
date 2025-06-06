# import re
# import uuid
# from datetime import datetime
# from typing import Optional

# from sqlalchemy import Boolean, DateTime, String, event
# from sqlalchemy.dialects.postgresql import UUID as pgUUID
# from sqlalchemy.engine import Connection
# from sqlalchemy.orm import Mapped, Mapper, mapped_column

# from app.db.base import Base


# def slugify(value: str) -> str:
#     """
#     Generate a URL-friendly slug from a string.

#     Replaces spaces/underscores with hyphens, lowercases, and removes
#     non-alphanumeric chars except hyphens.
#     """
#     value = re.sub(r"[\s_]+", "-", value.lower())
#     return re.sub(r"[^a-z0-9-]", "", value)


# class User(Base):
#     """
#     User SQLAlchemy model corresponding to user schemas.

#     Attributes
#     ----------
#     id : uuid.UUID
#         Unique user identifier (primary key).
#     first_name : Optional[str]
#         User's first name (nullable).
#     last_name : str
#         User's last name (required).
#     slug : Optional[str]
#         Unique URL-friendly slug.
#     email : str
#         Unique email address.
#     hashed_password : str
#         Hashed password.
#     country : Optional[str]
#         2-letter uppercase country code.
#     profile_pic : Optional[str]
#         URL or path to profile picture.
#     contact_number : Optional[str]
#         User contact number.
#     is_active : bool
#         Whether user account is active.
#     is_superuser : bool
#         System-level privileges flag.
#     is_admin : bool
#         Admin permissions flag (custom logic).
#     is_banned : bool
#         Ban/block status flag.
#     created_at : datetime
#         Creation timestamp.
#     updated_at : Optional[datetime]
#         Last update timestamp.
#     """

#     __tablename__ = "users"

#     id: Mapped[uuid.UUID] = mapped_column(
#         pgUUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         unique=True,
#         index=True,
#     )
#     first_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
#     last_name: Mapped[str] = mapped_column(String, nullable=False)
#     slug: Mapped[Optional[str]] = mapped_column(
#         String,
#         unique=True,
#         index=True,
#         nullable=True,
#     )
#     email: Mapped[str] = mapped_column(
#         String,
#         unique=True,
#         index=True,
#         nullable=False,
#     )
#     hashed_password: Mapped[str] = mapped_column(String, nullable=False)
#     country: Mapped[Optional[str]] = mapped_column(
#         String(length=2),
#         nullable=True,
#     )
#     profile_pic: Mapped[Optional[str]] = mapped_column(String, nullable=True)
#     contact_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)

#     is_active: Mapped[bool] = mapped_column(Boolean, default=True)
#     is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
#     is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
#     is_banned: Mapped[bool] = mapped_column(Boolean, default=False)

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=datetime.now
#     )
#     updated_at: Mapped[Optional[datetime]] = mapped_column(
#         DateTime(timezone=True), onupdate=datetime.now, nullable=True
#     )


# @event.listens_for(User, "before_insert")
# def generate_slug(
#     mapper: Mapper,
#     connection: Connection,
#     target: User,
# ) -> None:
#     """
#     Generate slug from last_name before insert if slug not set.
#     """
#     if not target.slug and target.last_name:
#         target.slug = slugify(target.last_name)
