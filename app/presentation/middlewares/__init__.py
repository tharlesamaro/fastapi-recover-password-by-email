from fastapi import FastAPI

from .cors_middleware import add_cors_middleware
from .db_middleware import add_db_middleware

__all__ = ["add_middlewares"]


def add_middlewares(app: FastAPI) -> None:
    add_cors_middleware(app)
    add_db_middleware(app)
