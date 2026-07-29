from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies.services import get_auth_service
from app.schemas import UserCreate, UserRead
from app.services import AuthService


router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(
    user_create: UserCreate,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> UserRead:
    return auth_service.register_user(user_create)
