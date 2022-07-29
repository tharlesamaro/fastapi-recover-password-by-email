from auth_router import router as auth_router
from fastapi import FastAPI
from user_router import router as user_router


def add_routes(app: FastAPI) -> None:
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])
    app.include_router(user_router, prefix="/users", tags=["User"])
