"""
User schema definitions using Pydantic models.

Defines input and output schemas for user-related operations such as
creation, update, and retrieval. Uses strict type annotations and
validation rules.
"""

import uuid
from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class BaseUser(BaseModel):
    """
    Basic user identity information.

    Attributes
    ----------
    first_name : Optional[str]
        User's first name (nullable).
    last_name : str
        User's last name (required).
    email : EmailStr
        Valid email address (required).
    """

    first_name: Optional[str] = None
    last_name: str
    email: EmailStr


class UserBase(BaseUser):
    """
    Extended user attributes for internal use.

    Attributes
    ----------
    country : Optional[str]
        2-letter ISO country code (optional).
    profile_pic : Optional[str]
        URL or path to profile picture (optional).
    contact_number : Optional[str]
        Phone number or contact info (optional).
    """

    country: Optional[str] = Field(None, min_length=2, max_length=2)
    profile_pic: Optional[str] = None
    contact_number: Optional[str] = None

    @field_validator("country")
    @classmethod
    def uppercase_country(cls, v: Optional[str]) -> Optional[str]:
        """
        Ensure country codes are stored in uppercase.

        Parameters
        ----------
        v : Optional[str]
            Country code value.

        Returns
        -------
        Optional[str]
            Uppercased country code, if provided.
        """
        if v:
            return v.upper()
        return v


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    Attributes
    ----------
    password : str
        Raw user password (min. 8 characters).
    """

    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """
    Schema for updating an existing user.

    All fields are optional to support partial updates.

    Attributes
    ----------
    first_name : Optional[str]
    last_name : Optional[str]
    country : Optional[str]
        2-letter ISO code (optional).
    profile_pic : Optional[str]
    contact_number : Optional[str]
    password : Optional[str]
        If provided, must be at least 8 characters long.
    is_admin : Optional[bool]
    is_banned : Optional[bool]
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country: Optional[str] = Field(None, min_length=2, max_length=2)
    profile_pic: Optional[str] = None
    contact_number: Optional[str] = None
    password: Annotated[Optional[str], Field(None, min_length=8)] = None
    is_admin: Optional[bool] = None
    is_banned: Optional[bool] = None


class UserOut(UserBase):
    """
    Schema for returning user data to clients.

    Attributes
    ----------
    id : uuid.UUID
        Unique user identifier.
    slug : Optional[str]
        URL-safe username or slug.
    is_active : bool
        Whether the user account is active.
    is_superuser : bool
        Whether the user has system-level privileges.
    is_admin : bool
        Whether the user has admin permissions (custom business logic).
    is_banned : bool
        Whether the user is banned or blocked.
    created_at : datetime
        Account creation timestamp.
    updated_at : Optional[datetime]
        Last updated timestamp.
    """

    id: uuid.UUID
    slug: Optional[str] = None
    is_active: bool
    is_superuser: bool
    is_admin: bool
    is_banned: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserOut):
    """
    Schema representing a user stored in the database.

    Attributes
    ----------
    hashed_password : str
        Hashed password stored in the database.
    """

    hashed_password: str


class PublicUserOut(BaseUser):
    """
    Public-facing user schema.

    Excludes private/sensitive fields such as email, contact number,
    is_superuser, etc.

    Attributes
    ----------
    first_name : Optional[str]
    last_name : str
    country : Optional[str]
    profile_pic : Optional[str]
    slug : Optional[str]
    """

    country: Optional[str] = Field(None, min_length=2, max_length=2)
    profile_pic: Optional[str] = None
    slug: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
