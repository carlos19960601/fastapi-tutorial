from pydantic import BaseModel, Field


class LoginRequet(BaseModel):
    email: str = Field(..., description="Email")  # ...表示该字段是必须的
    password: str = Field(..., description="Password")


class CreateUserRequest(BaseModel):
    email: str = Field(..., description="Email")
    password1: str = Field(..., description="Password1")
    password2: str = Field(..., description="Password2")
    nickname: str = Field(..., description="Nickname")