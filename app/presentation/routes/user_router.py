from typing import Any

from fastapi import APIRouter, status
from fastapi_pagination import Page, paginate

from app.data import UserCreateSchema, UserVO
from app.presentation.routes._responses import get_responses
from app.usecases import user_usecase

router = APIRouter()


@router.post(
    "",
    response_model=UserVO,
    status_code=status.HTTP_201_CREATED,
    responses=get_responses(status.HTTP_409_CONFLICT),
)
async def create_user(user_create: UserCreateSchema) -> Any:
    """
    Create a new user.
    """
    user_created = user_usecase.create(user_create)
    return user_created


@router.get(
    "",
    response_model=Page[UserVO],
    responses=get_responses(),
)
async def list_users() -> Any:
    """
    List paginated users.
    """
    users = user_usecase.all()
    return paginate(users)


@router.get(
    "/{user_id}",
    response_model=UserVO,
    responses=get_responses(status.HTTP_404_NOT_FOUND),
)
async def get_user(user_id: int) -> Any:
    """
    Get a user.
    """
    user = user_usecase.get(user_id)
    return user


@router.delete(
    "/{user_id}",
    response_model=UserVO,
    responses=get_responses(status.HTTP_404_NOT_FOUND),
)
async def delete_user(user_id: int) -> Any:
    """
    Delete a user.
    """
    user_deleted = user_usecase.delete(user_id)
    return user_deleted
