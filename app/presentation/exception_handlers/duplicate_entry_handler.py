from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.data.exceptions import DuplicateEntry


async def duplicate_entry_handler(
    _: Request, exc: DuplicateEntry
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exc)},
    )


def add_duplicate_entry_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        DuplicateEntry,
        duplicate_entry_handler,
    )
