from abc import ABC, abstractmethod

from app.user.domain.entity.user import User


# repo层的接口定义
class UserRepo(ABC):
    @abstractmethod
    async def get_users(self, limit: int = 12) -> list[User]:
        """获取用户列表"""

    @abstractmethod
    async def get_user_by_email_or_nickname(self, email: str, nickname: str) -> User:
        """通过邮箱或昵称获取用户"""

    @abstractmethod
    async def save(self, user: User) -> None:
        """保存用户"""

    async def get_user_by_email_and_password(self, email: str, password: str) -> User:
        """通过邮箱和密码获取用户"""
