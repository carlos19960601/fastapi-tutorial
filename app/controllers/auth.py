import re

from pydantic import EmailStr

from app.models import User
from app.repositories import UserRepository
from app.schemas.extras.token import Token
from core.controller import BaseController
from core.database import Propagation, Transactional
from core.exceptions.base import BadRequestException


class AuthController(BaseController[User]):
    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository

    # @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, email: EmailStr, password: str, username: str) -> User:
        user = await self.user_repository.get_by_email(email)
        if user:
            raise BadRequestException("User already exists with this email")
        user = await self.user_repository.get_by_username(username)

        if user:
            raise BadRequestException("User already exists with this username")

        return await self.user_repository.create(
            {
                "email": email,
                "password": password,
                "username": username,
            }
        )

    async def login(self, email: EmailStr, password: str) -> Token:
        user = await self.user_repository.get_by_email(email)

        if not user:
            raise BadRequestException("Invalid credentials")

        return Token(access_token="", refresh_token="")
