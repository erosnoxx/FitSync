from datetime import date, timedelta
from random import randint
import pytest
from uuid import uuid4
from src.application.dtos.input.auth.create.CreatePersonInputDto import CreatePersonInputDto
from src.application.usecases.auth.create.CreatePersonUseCase import CreatePersonUseCase
from src.exceptions.auth.InvalidFieldError import InvalidFieldError
from src.exceptions.auth.PersonAlreadyExistsError import PersonAlreadyExistsError
from src.exceptions.auth.UserNotExistsError import UserNotExistsError
from src.exceptions.common.UnauthorizedError import UnauthorizedError


@pytest.mark.create_person
def test_create_person_success(app, user):
    """Testa criação de pessoa"""

    input_dto = CreatePersonInputDto(
        user_id=user.id,
        first_name='Test',
        last_name='Silva',
        birthdate='2000-01-01',
        phone_number='11999248662')
    
    usecase: CreatePersonUseCase = app.usecases.create_person_usecase
    output = usecase.execute(input_dto=input_dto)

    assert output.person_entity is not None
    assert output.person_entity.full_name == f'{input_dto.first_name} {input_dto.last_name}'
    assert output.person_entity.birthdate == input_dto.birthdate
    assert output.person_entity.phone_number == input_dto.phone_number
    assert output.person_entity.user_id == user.id

@pytest.mark.create_person
def test_create_person_invalid_user(app):
    """Testa criação de pessoa com usuário inválido"""

    input_dto_invalid_user_id = CreatePersonInputDto(
        user_id=uuid4(),
        first_name='Test',
        last_name='Silva',
        birthdate='2000-01-01',
        phone_number='11999248662')
    
    usecase: CreatePersonUseCase = app.usecases.create_person_usecase

    with pytest.raises(UserNotExistsError) as excinfo:
        usecase.execute(input_dto=input_dto_invalid_user_id)
    
    assert 'Usuário não encontrado.' in  str(excinfo.value)
    assert '404' in  str(excinfo.value)

@pytest.mark.create_person
def test_create_person_underage(app, user):
    """Testa criação de pessoa com idade menor que 14 anos."""
    generate_young_birthdate = (date.today() - timedelta(days=randint(365, 365 * 13))).strftime('%Y-%m-%d')
    input_dto = CreatePersonInputDto(
        user_id=user.id,
        first_name='Teste',
        last_name='Menor',
        birthdate=generate_young_birthdate,  # Usuário com idade menor que 14
        phone_number='11999248662'
    )
    usecase: CreatePersonUseCase = app.usecases.create_person_usecase
    
    with pytest.raises(UnauthorizedError) as excinfo:
        usecase.execute(input_dto=input_dto)
    
    assert 'Usuário não atinge a idade necessária para a utilização do app' in str(excinfo.value)
    assert '401' in str(excinfo.value)

@pytest.mark.create_person
def test_create_person_with_existing_user(app, person):
    """Testa a criação de uma segunda pessoa para um usuário já vinculado."""

    # Define os dados para tentar criar uma nova `Person` com o mesmo `user_id` do `person`
    input_dto_duplicate = CreatePersonInputDto(
        user_id=person.user_id,  # Mesmo `user_id` da pessoa já existente
        first_name='Novo',
        last_name='Teste',
        birthdate='2005-05-05',
        phone_number='11999887766'
    )

    # Executa o caso de uso e verifica se a exceção `PersonAlreadyExistsError` é levantada
    usecase: CreatePersonUseCase = app.usecases.create_person_usecase

    with pytest.raises(PersonAlreadyExistsError) as excinfo:
        usecase.execute(input_dto=input_dto_duplicate)

    assert 'Já existe uma pessoa vinculada a este usuário.' in str(excinfo.value)
    assert '409' in str(excinfo.value)


@pytest.mark.create_person
def test_create_person_with_invalid_phone_number(app, user):
    """Testa a criação de pessoa com telefone inválido."""
    input_dto_invalid = CreatePersonInputDto(
        user_id=user.id,
        first_name='Teste',
        last_name='Inválido',
        birthdate='2005-05-05',
        phone_number='123456789'  # Telefone inválido
        )
    
    usecase: CreatePersonUseCase = app.usecases.create_person_usecase

    with pytest.raises(InvalidFieldError) as excinfo:
        usecase.execute(input_dto=input_dto_invalid)

    assert  'Número de telefone inválido.' in str(excinfo.value)
    assert '400' in  str(excinfo.value)
