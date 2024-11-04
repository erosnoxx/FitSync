from datetime import datetime
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils
from pythonwebtools.services.HashService import HashService
from src.application.contracts.data.repositories.auth.IUserRepository import IUserRepository
from src.application.dtos.input.auth.create.CreateUserInputDto import CreateUserInputDto
from src.application.dtos.output.auth.CreateUserOutputDto import CreateUserOutputDto
from src.domain.entities.auth.UserEntity import UserEntity
from src.exceptions.auth.InvalidFieldError import InvalidFieldError
from src.exceptions.auth.UserAlreadyExistsError import UserAlreadyExistsError
from src.exceptions.common.InternalServerError import InternalServerError


class CreateUserUseCase:
    def __init__(self,  repository: IUserRepository) -> None:
        self.repository = repository
    
    def execute(self, input_dto: CreateUserInputDto) -> CreateUserOutputDto:
        validate = ValidatorUtils()
        hash_service = HashService()
        
        if not validate.validate_email(email=input_dto.email):
            raise InvalidFieldError(message='Email inválido.')
        
        if not validate.validate_password(password=input_dto.password):
            raise InvalidFieldError(message='Senha inválida.')
        
        username_exists = self.repository.get_by_username(username=input_dto.username)
        if username_exists:
            raise UserAlreadyExistsError(message='Username já registrado.')
        
        email_exists = self.repository.get_by_email(email=input_dto.email)
        if email_exists:
            raise UserAlreadyExistsError(message='Email já registrado.')
        
        hashed_password = hash_service.hash_password(password=input_dto.password)

        try:
            user_entry = UserEntity(
                username=input_dto.username,
                email=input_dto.email,
                password_hash=hashed_password,
                is_verified=False,
                is_enabled=True,
                last_login=datetime.now())
            
            user_entity = self.repository.add(user_entry)
            return CreateUserOutputDto(user_entity=user_entity)
        except ValueError as ve:
            raise InvalidFieldError(message=ve)
        except Exception as e:
            raise InternalServerError(message=e)
