from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.auth.IUserRepository import IUserRepository
from src.domain.entities.auth.UserEntity import UserEntity


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        super().__init__(session, UserEntity)

    def get_by_email(self, email: str) -> UserEntity:
        return self.session.query(self.entity).filter(self.entity.email==email).first()

    def get_by_username(self, username: str) -> UserEntity:
        return self.session.query(self.entity).filter(self.entity.username==username).first()
