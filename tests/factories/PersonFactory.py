from tests.factories import *


class PersonFactory(SQLAlchemyModelFactory):
    class Meta:
        model = PersonEntity
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'
    
    user_id = None
    first_name = LazyAttribute(lambda _: fake.name())
    last_name = LazyAttribute(lambda _: fake.name())
    birthdate = LazyAttribute(lambda _: fake.date_of_birth())
    phone_number = '11999248662'
    avatar_url = LazyAttribute(lambda _: fake.url())
