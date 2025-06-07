"""
Unit tests for user schema validation.

This module contains tests for the `UserCreate` and `UserOut` Pydantic schemas,
ensuring proper validation logic such as required fields, email format, password
strength, and proper serialization of output data.
"""

import uuid
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from app.schemas.user import UserCreate, UserOut


def test_valid_user_create() -> None:
    """
    Test creating a valid UserCreate instance.

    Ensures that all fields are correctly assigned.
    """
    user = UserCreate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        country="US",
        profile_pic="https://example.com/pic.jpg",
        contact_number="+123456789",
        password="securepass123",
    )
    assert user.email == "john.doe@example.com"
    assert user.password == "securepass123"
    assert user.country == "US"


def test_invalid_email_user_create() -> None:
    """
    Test UserCreate with invalid email.

    Should raise ValidationError for malformed email.
    """
    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="invalid-email",
            password="securepass123",
            country="US",  # Added missing required argument
        )


def test_missing_required_fields_user_create() -> None:
    """
    Test UserCreate with missing required fields.

    Should raise ValidationError for missing last_name, email, password.
    """
    with pytest.raises(ValidationError):
        UserCreate()  # type: ignore


def test_short_password_user_create() -> None:
    """
    Test UserCreate with short password.

    Should raise ValidationError for password length < 8.
    """
    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            password="short",
            country="US",  # Added missing required argument
        )


def test_invalid_country_code_user_create() -> None:
    """
    Test UserCreate with invalid country code.

    Should raise ValidationError for >2-character country code.
    """
    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            password="securepassword123",
            country="USA",  # Invalid (more than 2 characters)
        )


def test_valid_user_out_schema() -> None:
    """
    Test creating a valid UserOut instance.

    Ensures all required and optional fields are validated and serialized.
    """
    user_out = UserOut(
        id=uuid.uuid4(),
        first_name="Alice",
        last_name="Smith",
        email="alice@example.com",
        country="GB",
        profile_pic=None,
        contact_number="+441234567890",
        slug="alice-smith",
        is_active=True,
        is_superuser=False,
        is_admin=True,
        is_banned=False,
        created_at=datetime.now(timezone.utc),
        updated_at=None,
    )

    assert user_out.slug == "alice-smith"
    assert isinstance(user_out.created_at, datetime)
    assert user_out.is_active is True
    assert user_out.is_admin is True
    assert user_out.is_banned is False
