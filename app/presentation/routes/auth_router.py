from typing import Any

from fastapi import APIRouter

from app.data import AuthSchema, AuthVO, MsgVO, UserEmailSchema, UserResetPasswordSchema
from app.presentation.routes._responses import HTTP_RESPONSES, get_responses
from app.usecases import auth_usecase

router = APIRouter()


@router.post(
    "/token",
    response_model=AuthVO,
    responses=get_responses(),
)
async def token(auth_schema: AuthSchema) -> Any:
    """User authentication"""
    return auth_usecase.token(auth_schema)


@router.post(
    "/password-recovery",
    response_model=MsgVO,
    responses={500: HTTP_RESPONSES.get("500")},
)
async def recover_password(input_data: UserEmailSchema) -> Any:
    """
    Password Recovery
    """
    return await auth_usecase.recover_password(input_data.email)


@router.post(
    "/reset-password",
    response_model=MsgVO,
    responses={
        400: HTTP_RESPONSES.get("400"),
        404: HTTP_RESPONSES.get("404"),
        500: HTTP_RESPONSES.get("500"),
    },
)
def reset_password(input_data: UserResetPasswordSchema) -> Any:
    """
    Reset password
    """
    return auth_usecase.reset_password(input_data.token, input_data.password)
