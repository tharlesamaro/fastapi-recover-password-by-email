from fastapi import FastAPI

from .duplicate_entry_handler import add_duplicate_entry_exception_handler
from .invalid_credentials_handler import (
    add_invalid_credentials_exception_handler,
)
from .invalid_token_handler import add_invalid_token_exception_handler
from .no_result_found_handler import add_no_result_found_exception_handler


def add_exception_handlers(app: FastAPI) -> None:
    add_duplicate_entry_exception_handler(app)
    add_invalid_credentials_exception_handler(app)
    add_invalid_token_exception_handler(app)
    add_no_result_found_exception_handler(app)
