from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.data.exceptions import InvalidCredentials


async def invalid_credentials_handler(
    _: Request, exc: InvalidCredentials
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": str(exc)},
        headers={"WWW-Authenticate": "Bearer"},
    )


def add_invalid_credentials_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        InvalidCredentials,
        invalid_credentials_handler,
    )
