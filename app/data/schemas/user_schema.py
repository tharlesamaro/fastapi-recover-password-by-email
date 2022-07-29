import re
from typing import Any

from pydantic import BaseModel, EmailStr, validator


def matchpwd(cls: type, v: str, values: dict[str, Any]) -> str:
    if "password" in values and v != values["password"]:
        raise ValueError("Passwords do not match")
    return v


def checkpwd(cls: type, v: str) -> str:
    if len(v) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if not re.search(r"\d", v):
        raise ValueError("Password must be at least one digit")

    if not re.search(r"[A-Z]", v):
        raise ValueError("Password must have at least one uppercase letter")

    if not re.search(r"[a-z]", v):
        raise ValueError("Password must have at least one lowercase letter")

    if not re.search(r"\W", v):
        raise ValueError("Password must have at least one special character")

    return v


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    password_confirmation: str

    # validators
    _matchpwd_password_confirmation = validator(
        "password_confirmation", pre=True, allow_reuse=True
    )(matchpwd)

    _checkpwd_password = validator("password", pre=True, allow_reuse=True)(checkpwd)


class UserResetPasswordSchema(BaseModel):
    token: str
    password: str
    password_confirmation: str

    # validators
    _matchpwd_password_confirmation = validator(
        "password_confirmation", pre=True, allow_reuse=True
    )(matchpwd)

    _checkpwd_password = validator("password", pre=True, allow_reuse=True)(checkpwd)


class UserEmailSchema(BaseModel):
    email: EmailStr
