from pydantic import BaseModel, Field
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    nickname: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    @classmethod
    def create(cls, *, email: str, password: str, nickname: str):
        return cls(email=email, password=password, nickname=nickname)


class UserRead(BaseModel):
    id: int = Field(..., title="用户ID")
    email: str = Field(..., title="邮箱")
    nickname: str = Field(..., title="昵称")
