from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.auth.UserEntity import UserEntity


class IUserRepository(ABC, BaseRepository[UserEntity]):

    def get_by_email(self, email: str) -> UserEntity:
        pass
    
    def get_by_username(self, username: str) -> UserEntity:
        pass
