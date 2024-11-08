from flask import Flask
from src.application.extensions.AppConfig import AppConfig
from src.application.extensions.AuthManager import AuthManager
from src.application.extensions.Globals import Globals
from src.application.extensions.Settings import Settings
from src.application.extensions.Api import Api


class Initializer:
    def __init__(self, app: Flask) -> None:
        AppConfig(app=app)
        Settings(app=app)
        Globals(app=app)
        AuthManager(app=app)
        
        Api(app=app)
