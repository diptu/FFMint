"""User model definition."""

from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, constr
from pydantic_extra_types.country import CountryAlpha2

PasswordStr: type = constr(min_length=8)


class User(BaseModel):
    """
    Represents a user in the system.

    Attributes
    ----------
    id : UUID
        Unique identifier for the user.
    first_name : str
        User's first name.
    last_name : str
        User's last name.
    email : EmailStr
        User's email address.
    password : PasswordStr
        Password with minimum length of 8 characters.
    country : CountryAlpha2
        ISO 3166-1 alpha-2 country code.
    """

    id: UUID = Field(..., description="Unique identifier for the user")
    first_name: str = Field(description="User's first name")
    last_name: str = Field(..., description="User's last name")
    email: EmailStr = Field(..., description="User's email address")
    password: PasswordStr = Field(..., description="Password (min 8 chars)")
    country: CountryAlpha2 = Field(description="country code")
