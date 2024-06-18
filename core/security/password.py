from passlib.context import CryptContext
from typing_extensions import deprecated


class PasswordHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str) -> str:
        return PasswordHandler.pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return PasswordHandler.pwd_context.verify(plain_password, hashed_password)
