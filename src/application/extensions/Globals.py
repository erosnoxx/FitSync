from flask import Flask

from src.application.config.GlobalControllers import GlobalControllers
from src.application.config.GlobalRepositories import GlobalRepositories
from src.application.config.GlobalUseCases import GlobalUseCases


class Globals:
    def __init__(self, app: Flask) -> None:
        app.repositories = GlobalRepositories()
        app.usecases = GlobalUseCases(
            repositories=app.repositories)
        app.controllers = GlobalControllers()
