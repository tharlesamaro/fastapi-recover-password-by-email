from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.config import app_config
from app.presentation import (
    add_exception_handlers,
    add_middlewares,
    add_routes,
)

app_kwargs = {
    "name": app_config.APP_NAME,
    "description": app_config.APP_DESCRIPTION,
    "version": 1.0,
    "env": app_config.APP_ENV,
}

app = FastAPI(**app_kwargs)
app.add_api_route("/", lambda: app_kwargs, include_in_schema=False)

add_exception_handlers(app)
add_middlewares(app)
add_routes(app)
add_pagination(app)
