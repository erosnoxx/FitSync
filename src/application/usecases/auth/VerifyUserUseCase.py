from pythonwebtools.utils.ValidatorUtils import ValidatorUtils
from pythonwebtools.services.HashService import HashService
from src.application.contracts.data.repositories.auth.IUserRepository import IUserRepository
from src.application.dtos.input.auth.create.VerifyUserInputDto import VerifyUserInputDto
from src.application.dtos.output.auth.VerifyUserOutputDto import VerifyUserOutputDto
from src.exceptions.auth.InvalidFieldError import InvalidFieldError
from src.exceptions.auth.UserNotExistsError import UserNotExistsError
from src.exceptions.common.InternalServerError import InternalServerError
from src.exceptions.common.UnauthorizedError import UnauthorizedError


class VerifyUserUseCase:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository
    
    def execute(self, input_dto: VerifyUserInputDto) -> VerifyUserOutputDto:
        try:
            validate = ValidatorUtils()
            hash_service = HashService()

            if not validate.validate_password(password=input_dto.password):
                raise InvalidFieldError('Senha inválida.')
            
            user_entity = self.repository.get_by_username(username=input_dto.username)
            if not user_entity:
                raise UserNotExistsError('Nome de usuário inválido.')
            
            if not hash_service.verify_password(
                hashed_password=user_entity.password_hash,
                provided_password=input_dto.password):
                raise UnauthorizedError('Senha incorreta.')
            
            return VerifyUserOutputDto(user_entity=user_entity)
        except InvalidFieldError:
            raise
        except UserNotExistsError:
            raise
        except UnauthorizedError:
            raise
        except Exception as e:
            raise InternalServerError(message=str(e))
