from pydantic import BaseModel, Field
from sqlalchemy import desc


class CurrentUser(BaseModel):
    id: int = Field(None, description="User ID")

    class Config:
        validate_assignment = True
