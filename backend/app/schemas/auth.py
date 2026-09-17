from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    username: str | None = Field(default=None, max_length=100)


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    username: str | None
    auth_provider: str

    model_config = ConfigDict(from_attributes=True)