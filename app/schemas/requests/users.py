import re

from pydantic import BaseModel, EmailStr, Field, constr, field_validator


class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)
    username: str = Field(..., min_length=3, max_length=64)

    @field_validator("password")
    @classmethod
    def password_must_contain_special_characters(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain at least one special character")

        return v

    @field_validator("password")
    @classmethod
    def password_must_contain_numbers(cls, v):
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one number")

        return v

    @field_validator("password")
    @classmethod
    def password_must_contain_uppercase_letters(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")

        return v

    @field_validator("password")
    @classmethod
    def password_must_contain_lowercase_letters(cls, v):
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")

        return v

    @field_validator("username")
    @classmethod
    def username_must_not_contain_special_characters(cls, v):
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")

        return v


class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str
