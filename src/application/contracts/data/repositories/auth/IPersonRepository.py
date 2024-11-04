from abc import ABC
from uuid import UUID
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.auth.PersonEntity import PersonEntity


class IPersonRepository(ABC, BaseRepository[PersonEntity]):
    def get_by_user_id(self, user_id: UUID) -> PersonEntity:
        pass
