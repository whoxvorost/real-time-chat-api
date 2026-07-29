from typing import Annotated

from fastapi import Depends

from app.dependencies.repositories import get_user_repository
from app.repositories import UserRepository
from app.services import AuthService


def get_auth_service(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> AuthService:
    return AuthService(user_repository)
