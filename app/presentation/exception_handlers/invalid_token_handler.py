from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.data.exceptions import InvalidToken


async def invalid_token_handler(_: Request, exc: InvalidToken) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)},
    )


def add_invalid_token_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        InvalidToken,
        invalid_token_handler,
    )
