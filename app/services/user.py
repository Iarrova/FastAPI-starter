from uuid import UUID

from app.exceptions.exceptions import ConflictException, NotFoundException
from app.models.user import User, UserCreate
from app.repositories.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, data: UserCreate):
        if self.repository.get_by_email(data.email):
            raise ConflictException("Email already registered")

        return self.repository.create(data)

    def get(self, id: UUID) -> User:
        user: User | None = self.repository.get(id)
        if not user:
            raise NotFoundException("User", id)

        return user
