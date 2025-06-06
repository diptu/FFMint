"""
Tests for the password hashing and verification functions
in the app.services.security module.
"""

from app.services import security


def test_password_hash_and_verify() -> None:
    """
    Test password hashing and verification.

    Verifies:
    - Hashed value is different from raw password.
    - Correct password validates.
    - Wrong password fails.
    """
    raw: str = "my_secure_password"
    hashed: str = security.get_password_hash(raw)

    assert hashed != raw
    assert security.verify_password(raw, hashed)
    assert not security.verify_password("wrong_password", hashed)
