from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.data.exceptions import NoResultFound


async def no_result_found_handler(
    _: Request, exc: NoResultFound
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )


def add_no_result_found_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        NoResultFound,
        no_result_found_handler,
    )
