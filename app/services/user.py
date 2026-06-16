from uuid import UUID

from app.exceptions.exceptions import ConflictException, NotFoundException
import bcrypt
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserLogin


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, data: UserCreate):
        if self.repository.get_by_email(data.email):
            raise ConflictException("Email already registered")

        data.password = hash_password(data.password)

        return self.repository.create(data)

    def get(self, id: UUID) -> User:
        user: User | None = self.repository.get(id)
        if not user:
            raise NotFoundException("User", id)

        return user

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password_bytes.decode("utf-8")


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
