from uuid import UUID
from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.auth.IPersonRepository import IPersonRepository
from src.domain.entities.auth.PersonEntity import PersonEntity


class PersonRepository(IPersonRepository):
    def __init__(self, session: Session):
        super().__init__(session, PersonEntity)

    def get_by_user_id(self, user_id: UUID) -> PersonEntity:
        return self.session.query(self.entity).filter(self.entity.user_id == user_id).first()
