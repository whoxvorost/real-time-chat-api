from fastapi import HTTPException, status

from app.core.security import create_access_token, get_password_hash, verify_password
from app.models import User
from app.repositories import UserRepository
from app.schemas import LoginRequest, UserCreate


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, user_create: UserCreate) -> User:
        if self.user_repository.get_by_email(user_create.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        if self.user_repository.get_by_username(user_create.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )

        hashed_password = get_password_hash(user_create.password)

        return self.user_repository.create(
            email=user_create.email,
            username=user_create.username,
            hashed_password=hashed_password,
        )

    def login_user(self, login_request: LoginRequest) -> str:
        user = self.user_repository.get_by_email(login_request.email)

        if not user or not verify_password(
            login_request.password, user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        return create_access_token(subject=str(user.id))
