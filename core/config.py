import os

from pydantic import RedisDsn
from pydantic_settings import BaseSettings


# 如果继承 BaseSettings 会从环境变量中读取非关键字参数赋值
class Config(BaseSettings):
    ENV: str = "dev"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    SECRET_KEY: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24
    REDIS_URL: RedisDsn = "redis://localhost:6379/0"


class DevConfig(Config): ...


class ProdConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "dev")
    config_type = {"dev": DevConfig(), "prod": ProdConfig()}

    return config_type[env]


config: Config = get_config()
