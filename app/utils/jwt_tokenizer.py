from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

import jwt
from jwt.exceptions import (
    DecodeError,
    ExpiredSignatureError,
    InvalidSignatureError,
)
from pydantic import EmailStr

from app.data import User, settings
from app.data.models import User


class JwtTokenizer:
    def __init__(self) -> None:
        self.algorithm = settings.JWT_ALGORITHM
        self.jwt_secret = settings.JWT_SECRET
        self.jwt_expire_hours = settings.JWT_EXPIRE_HOURS
        self.email_reset_token_expire_hours = (
            settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS
        )

    def _get_registered_claim_names(
        self, expire_hours: int
    ) -> dict[str, datetime | str]:
        delta = timedelta(hours=expire_hours)
        now = datetime.utcnow()
        expires = now + delta
        exp = expires.timestamp()

        return {"exp": exp, "iat": now, "jti": str(uuid4()), "nbf": now}

    def encode(
        self, payload: dict[str, Any], registered_claim_names: dict[str, Any]
    ) -> str:
        payload = payload.copy()
        payload.update(registered_claim_names)
        token = jwt.encode(
            payload=payload,
            key=self.jwt_secret,
            algorithm=self.algorithm,
        )
        return token

    def decode(self, token: str) -> dict[str, Any] | None:
        try:
            return jwt.decode(
                jwt=token,
                key=self.jwt_secret,
                algorithms=[self.algorithm],
                options={"require": ["exp", "iat"]},
            )
        except (InvalidSignatureError, ExpiredSignatureError, DecodeError):
            return None

    def generate_access_token(self, user_id: int) -> str:
        payload = {"uid": user_id}
        registered_claim_names = self._get_registered_claim_names(
            self.jwt_expire_hours
        )
        token = self.encode(payload, registered_claim_names)
        return token

    def generate_password_reset_token(
        self, user_id: int, user_email: EmailStr
    ) -> str:
        payload = {"uid": user_id, "sub": user_email}
        registered_claim_names = self._get_registered_claim_names(
            self.email_reset_token_expire_hours
        )
        token = self.encode(payload, registered_claim_names)
        return token
