import os
import pytest
from dotenv import load_dotenv
from app import App
from src.application.extensions.Settings import db
from tests.factories.PersonFactory import PersonFactory
from tests.factories.UserFactory import UserFactory

load_dotenv()


@pytest.fixture(scope='class')
def app():
    app = App().create_app()
    app.config.from_mapping({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI_TEST')
    })

    with app.app_context():
        db.create_all()
        
        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='class')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='class')
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='class')
def user(app):
    user = UserFactory.create()
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture(scope='class')
def person(app, user):
    person = PersonFactory.create(user_id=user.id)
    db.session.add(person)
    db.session.commit()
    return person
