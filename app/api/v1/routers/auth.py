from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies.services import get_auth_service
from app.schemas import LoginRequest, TokenResponse, UserCreate, UserRead
from app.services import AuthService


router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(
    user_create: UserCreate,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> UserRead:
    return auth_service.register_user(user_create)


@router.post("/login", response_model=TokenResponse)
def login(
    login_request: LoginRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> TokenResponse:
    access_token = auth_service.login_user(login_request)
    return TokenResponse(access_token=access_token)
