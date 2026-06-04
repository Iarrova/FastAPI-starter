import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str


class User(UserBase, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(unique=True)
    password: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserPublic(UserBase):
    id: uuid.UUID
