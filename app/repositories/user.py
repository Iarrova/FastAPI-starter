from uuid import UUID

import bcrypt
from sqlmodel import Session, select

from app.models.user import User, UserCreate


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, create: UserCreate) -> User:
        user = User(
            name=create.name,
            email=create.email,
            password=hash_password(create.password),
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get(self, id: UUID) -> User | None:
        return self.session.get(User, id)

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password_bytes.decode("utf-8")
