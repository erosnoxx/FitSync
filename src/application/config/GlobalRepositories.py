from sqlalchemy.orm import Session
from src.application.extensions.Settings import db
from src.data.repositories.auth.PersonRepository import PersonRepository
from src.data.repositories.auth.UserRepository import UserRepository


class GlobalRepositories:
    def __init__(self):
        _session: Session = db.session

        self.user_repository = UserRepository(session=_session)
        self.person_repository = PersonRepository(session=_session)
