from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.data import settings


def add_db_middleware(app: FastAPI) -> None:
    session_args = {"autocommit": False, "autoflush": False}
    db_url = settings.DB_CONN_STR

    app.add_middleware(
        DBSessionMiddleware,
        db_url=db_url,
        session_args=session_args,
    )
