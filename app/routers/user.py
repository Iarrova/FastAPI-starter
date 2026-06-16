from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from app.dependencies import get_user_service
from app.schemas.user import UserCreate, UserLogin, UserPublic
from app.services.user import UserService

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserPublic)
async def register_user(
    user_create: UserCreate, service: UserService = Depends(get_user_service)
):
    return service.register(user_create)


@router.post("/login", response_model=UserPublic)
async def login(
    user_login: UserLogin, service: UserService = Depends(get_user_service)
):
    return service.login(user_login)


@router.get("/{id}", response_model=UserPublic)
async def get_user(
    id: Annotated[UUID, Path(title="The ID of the user to get")],
    service: UserService = Depends(get_user_service),
):
    return service.get(id)
