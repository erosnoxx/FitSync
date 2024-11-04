import pytest
from pythonwebtools.services.HashService import HashService
from src.application.dtos.input.auth.create.CreateUserInputDto import CreateUserInputDto
from src.application.usecases.auth.create.CreateUserUseCase import CreateUserUseCase
from src.exceptions.auth.InvalidFieldError import InvalidFieldError
from src.exceptions.auth.UserAlreadyExistsError import UserAlreadyExistsError

hash_service = HashService()


@pytest.mark.create_user
def test_create_user_success(app):
    """Testa a criação bem-sucedida de um usuário com dados válidos."""
    input_dto = CreateUserInputDto(
        username='new_user',
        email='new_valid@email.com',
        password='StrongPassword5@')
    
    usecase: CreateUserUseCase = app.usecases.create_user_usecase

    output = usecase.execute(input_dto=input_dto)

    assert output.user_entity is not None
    assert output.user_entity.username == input_dto.username
    assert output.user_entity.email == input_dto.email
    assert hash_service.verify_password(
        hashed_password=output.user_entity.password_hash,
        provided_password=input_dto.password)

@pytest.mark.create_user
def test_create_user_duplicate_username(app, user):
    """Testa a criação de um usuário com um nome de usuário já existente."""
    input_dto_duplicate_username = CreateUserInputDto(
        username=user.username,
        email='different_email@email.com',
        password='StrongPassword5@')
    
    usecase: CreateUserUseCase = app.usecases.create_user_usecase

    with pytest.raises(UserAlreadyExistsError) as excinfo:
        usecase.execute(input_dto=input_dto_duplicate_username)

    assert 'Username já registrado.' in str(excinfo.value)
    assert '409' in str(excinfo.value)

@pytest.mark.create_user
def test_create_user_duplicate_email(app, user):
    """Testa a criação de um usuário com um email já existente."""
    input_dto_duplicate_email = CreateUserInputDto(
        username='another_username',
        email=user.email,
        password='AnotherStrongPassword5@')

    usecase: CreateUserUseCase = app.usecases.create_user_usecase

    with pytest.raises(UserAlreadyExistsError) as excinfo:
        usecase.execute(input_dto=input_dto_duplicate_email)

    assert 'Email já registrado.' in str(excinfo.value)
    assert '409' in str(excinfo.value)

@pytest.mark.create_user
def test_create_user_invalid_email(app):
    """Testa a criação de um usuário com um email inválido."""
    input_dto_invalid_email = CreateUserInputDto(
        username='new_user',
        email='invalid-email',
        password='StrongPassword5@')

    usecase: CreateUserUseCase = app.usecases.create_user_usecase

    with pytest.raises(InvalidFieldError) as excinfo:
        usecase.execute(input_dto=input_dto_invalid_email)

    assert 'Email inválido.' in str(excinfo.value)

@pytest.mark.create_user
def test_create_user_weak_password(app):
    """Testa a criação de um usuário com uma senha fraca."""
    input_dto_weak_password = CreateUserInputDto(
        username='another_user',
        email='another_valid@email.com',
        password='weak')

    usecase: CreateUserUseCase = app.usecases.create_user_usecase

    with pytest.raises(InvalidFieldError) as excinfo:
        usecase.execute(input_dto=input_dto_weak_password)

    assert 'Senha inválida.' in str(excinfo.value)
    assert '400' in str(excinfo.value)
