from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories import UserRepository


def get_user_repository(db: Annotated[Session, Depends(get_db)]) -> UserRepository:
    return UserRepository(db)
