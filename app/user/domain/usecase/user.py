from abc import ABC, abstractmethod
from typing import Optional

from app.user.application.dto import LoginResponseDTO
from app.user.domain.command import CreateUserCommand
from app.user.domain.entity.user import User


# service层的接口定义
class UserUseCase(ABC):
    @abstractmethod
    async def get_user_list(
        self, *, limit: int = 12, prev: Optional[int] = None
    ) -> list[User]:
        """获取用户列表"""

    @abstractmethod
    async def create_user(self, command: CreateUserCommand) -> None:
        """创建用户"""

    @abstractmethod
    async def login(self, email: str, password: str) -> LoginResponseDTO:
        """用户登录"""
