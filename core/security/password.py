from passlib.context import CryptContext
from typing_extensions import deprecated


class PasswordHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str) -> str:
        return PasswordHandler.pwd_context.hash(password)

    def verify(hass)