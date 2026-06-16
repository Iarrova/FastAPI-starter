import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: EmailStr = Field(unique=True)
    password: str
