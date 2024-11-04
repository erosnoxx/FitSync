from flask import Flask
from src.application.extensions.AppConfig import AppConfig
from src.application.extensions.Globals import Globals
from src.application.extensions.Settings import Settings


class Initializer:
    def __init__(self, app: Flask) -> None:
        AppConfig(app=app)
        Settings(app=app)
        Globals(app=app)
