from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Settings:
    def __init__(self, app: Flask) -> None:
        db.init_app(app=app)
        Migrate(app=app, db=db)
