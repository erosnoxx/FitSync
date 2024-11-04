from datetime import date, datetime
from pythonwebtools.utils.ValidatorUtils import ValidatorUtils
from src.application.contracts.data.repositories.auth.IPersonRepository import IPersonRepository
from src.application.contracts.data.repositories.auth.IUserRepository import IUserRepository
from src.application.dtos.input.auth.create.CreatePersonInputDto import CreatePersonInputDto
from src.application.dtos.output.auth.CreatePersonOutputDto import CreatePersonOutputDto
from src.domain.entities.auth.PersonEntity import PersonEntity
from src.exceptions.auth.InvalidFieldError import InvalidFieldError
from src.exceptions.auth.PersonAlreadyExistsError import PersonAlreadyExistsError
from src.exceptions.auth.UserNotExistsError import UserNotExistsError
from src.exceptions.common.InternalServerError import InternalServerError
from src.exceptions.common.UnauthorizedError import UnauthorizedError


class CreatePersonUseCase:
    def __init__(self,
                repository: IPersonRepository,
                u_repository: IUserRepository) -> None:
        self.repository = repository
        self.u_repository = u_repository
    
    def execute(self, input_dto: CreatePersonInputDto) -> CreatePersonOutputDto:
        user_exists = self.u_repository.get(input_dto.user_id)
        if not user_exists:
            raise UserNotExistsError(message='Usuário não encontrado.')
        
        existing_person = self.repository.get_by_user_id(user_id=input_dto.user_id)
        if existing_person:
            raise PersonAlreadyExistsError(message='Já existe uma pessoa vinculada a este usuário.')

        validate = ValidatorUtils()
        if not validate.phone_number_validator(phone_number=input_dto.phone_number):
            raise InvalidFieldError(message='Número de telefone inválido.')

        if isinstance(input_dto.birthdate, str):
            input_dto.birthdate = datetime.strptime(input_dto.birthdate, '%Y-%m-%d').date()
        
        try:
            person_entry = PersonEntity(
                user_id=input_dto.user_id,
                first_name=input_dto.first_name,
                last_name=input_dto.last_name,
                phone_number=input_dto.phone_number,
                birthdate=input_dto.birthdate)
            
            if person_entry.age < 14:
                raise UnauthorizedError(message='Usuário não atinge a idade necessária para a utilização do app.')

            person_entity = self.repository.add(person_entry)
            return CreatePersonOutputDto(person_entity=person_entity)
        except ValueError as ve:
            raise InvalidFieldError(message=ve)
        except UnauthorizedError:
            raise
        except Exception as e:
            raise InternalServerError(message=e)
