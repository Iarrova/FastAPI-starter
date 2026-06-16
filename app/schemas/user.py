import uuid

from pydantic import BaseModel, EmailStr


class UserPublic(BaseModel):
    id: uuid.UUID
    name: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
