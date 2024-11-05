from src.application.config.GlobalRepositories import GlobalRepositories
from src.application.usecases.auth.CreatePersonUseCase import CreatePersonUseCase
from src.application.usecases.auth.CreateUserUseCase import CreateUserUseCase
from src.application.usecases.auth.VerifyUserUseCase import VerifyUserUseCase


class GlobalUseCases:
    def __init__(self, repositories: GlobalRepositories):
        self.create_user_usecase = CreateUserUseCase(repository=repositories.user_repository)
        self.create_person_usecase = CreatePersonUseCase(
            repository=repositories.person_repository,
            u_repository=repositories.user_repository)
        self.verify_user_usecase = VerifyUserUseCase(repository=repositories.user_repository)
