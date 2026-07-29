from app.core.security import get_password_hash
from app.repositories import UserRepository
from app.schemas import UserCreate
from app.models import User


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, user_create: UserCreate) -> User:
        hashed_password = get_password_hash(user_create.password)

        return self.user_repository.create(
            email=user_create.email,
            username=user_create.username,
            hashed_password=hashed_password,
        )
