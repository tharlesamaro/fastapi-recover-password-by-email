from auth_router import router as auth_router
from fastapi import FastAPI


def add_routes(app: FastAPI) -> None:
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])
