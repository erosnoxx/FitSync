from tests.factories import *
from werkzeug.security import generate_password_hash


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = UserEntity
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    username = 'user01'
    email = 'valid@email.com'
    password_hash = LazyAttribute(lambda _: generate_password_hash(fake.password()))
    is_verified = True
    is_enabled = True
    last_login = LazyAttribute(lambda _: fake.date_time_between(start_date="-1y", end_date="now"))
