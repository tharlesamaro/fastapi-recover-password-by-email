from typing import Any, Coroutine

from pydantic import EmailStr

from app.config import auth_config
from app.data import AuthSchema, AuthVO
from app.data.exceptions import InvalidCredentials, InvalidToken, NoResultFound
from app.infra.repositories import UserRepository
from app.utils import hasher, tokenizer


def token(auth: AuthSchema) -> AuthVO:
    user = UserRepository().get_by(email=auth.email)

    invalid_credentials = (
        not user
        or not user.is_active
        or not hasher.verify(user.password, auth.password)
    )

    if invalid_credentials:
        raise InvalidCredentials()

    access_token = tokenizer.generate_access_token(user.id)

    return AuthVO(
        token_type=auth_config.JWT_TOKEN_TYPE,
        expires_in=auth_config.JWT_EXPIRE_HOURS,
        access_token=access_token,
    )
