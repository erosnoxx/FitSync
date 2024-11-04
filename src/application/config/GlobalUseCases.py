from src.application.config.GlobalRepositories import GlobalRepositories
from src.application.usecases.auth.create.CreatePersonUseCase import CreatePersonUseCase
from src.application.usecases.auth.create.CreateUserUseCase import CreateUserUseCase


class GlobalUseCases:
    def __init__(self, repositories: GlobalRepositories):
        self.create_user_usecase = CreateUserUseCase(repository=repositories.user_repository)
        self.create_person_usecase = CreatePersonUseCase(
            repository=repositories.person_repository,
            u_repository=repositories.user_repository)
