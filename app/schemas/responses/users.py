from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    email: str = Field(..., examples=["user@example.com"])
    username: str = Field(..., examples=["user"])
