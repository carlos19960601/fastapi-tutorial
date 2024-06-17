from enum import Enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.mixins import TimestampMixin
from core.database.session import Base


class UserPermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    @classmethod
    def create(cls, *, email: str, password: str, nickname: str):
        return cls(email=email, password=password, nickname=nickname)
