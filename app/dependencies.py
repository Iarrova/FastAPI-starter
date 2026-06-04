from fastapi import Depends
from sqlmodel import Session

from app.database import get_session
from app.repositories.user import UserRepository
from app.services.user import UserService


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(session)


def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)
