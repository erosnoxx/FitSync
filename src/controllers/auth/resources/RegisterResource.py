from uuid import UUID
from flask import Response, current_app, make_response, request
from flask_restx import Resource
from src.application.usecases.auth.create.CreatePersonUseCase import CreatePersonUseCase
from src.application.usecases.auth.create.CreateUserUseCase import CreateUserUseCase
from src.controllers.auth import namespace
from src.application.dtos.input.auth.create.CreatePersonInputDto import CreatePersonInputDto
from src.application.dtos.input.auth.create.CreateUserInputDto import CreateUserInputDto
from src.application.schemas.auth.RegisterSchemas import RegisterSchemas, api
from src.application.schemas.common.ErrorSchemas import ErrorSchemas
from src.infra.utils.handlers.ErrorHandler import ErrorHandler


class RegisterResource(Resource):
    @namespace.doc('Endpoint de criação de usuário')
    @namespace.expect(RegisterSchemas.register_user_schema())
    @namespace.response(201, 'Created', RegisterSchemas.register_user_response())
    @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
    @namespace.response(403, 'Forbidden', ErrorSchemas.http_403())
    @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
    @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
    @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
    @ErrorHandler.handle_exceptions
    def post(self) -> Response:
        data = request.json

        user_input_dto = CreateUserInputDto()
        user_input_dto.set_attributes(**data)
        user_usecase: CreateUserUseCase = current_app.usecases.create_user_usecase
        user_output_dto = user_usecase.execute(input_dto=user_input_dto)

        person_input_dto = CreatePersonInputDto()
        person_input_dto.set_attributes(**data)
        person_input_dto.user_id = user_output_dto.user_entity.id
        person_usecase: CreatePersonUseCase = current_app.usecases.create_person_usecase
        person_usecase.execute(input_dto=person_input_dto)

        return self.make_success_response(id=user_output_dto.user_entity.id)

    def make_success_response(self, id: UUID) -> Response:
        response_data = {
                'id': str(id),
                'success': True,
                'message': 'Usuário registrado com sucesso.',
                'statuscode': 201}
        response = make_response(response_data, 201)
        response.headers['Location'] = f'{api.prefix}/users/{str(id)}'
        response.headers['Content-Type'] = 'application/json'
        return response
