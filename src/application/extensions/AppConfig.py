import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


class AppConfig:
    def __init__(self, app: Flask) -> None:
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG')
        app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        if 'PYTEST_CURRENT_TEST' in os.environ:
            app.config['TESTING'] = True

        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')

        if app.config['TESTING']:
            app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI_TEST')
