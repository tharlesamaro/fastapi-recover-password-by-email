from typing import Any, Coroutine

from pydantic import EmailStr

from app.config import auth_config
from app.data import AuthSchema, AuthVO
from app.data.exceptions import InvalidCredentials, NoResultFound
from app.infra.email import SendResetPasswordEmail
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


async def recover_password(
    email: EmailStr,
) -> Coroutine[Any, Any, dict[str, str]]:
    user = UserRepository().get_by(email=email)

    if not user:
        raise NoResultFound("User")

    password_reset_token = tokenizer.generate_password_reset_token(
        user.id, user.email
    )

    await SendResetPasswordEmail.send(user, password_reset_token)

    return {
        "msg": "A password reset message will be sent to the email provided."
    }
