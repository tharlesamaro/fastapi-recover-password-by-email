from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.data.exceptions import InvalidToken
from app.data.models import User
from app.infra.repositories import UserRepository
from app.utils import tokenizer

http_bearer = HTTPBearer()


async def auth_user(
    http_auth: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> User:
    token = http_auth.credentials
    decoded_token = tokenizer.decode(token)

    invalid_token = not (
        decoded_token
        and "uid" in decoded_token
        and (user := UserRepository().get(decoded_token["uid"]))
    )

    if invalid_token:
        raise InvalidToken()

    return user
