from uuid import UUID
from flask import Response, current_app, make_response, request
from flask_login import login_user
from flask_restx import Resource
from src.application.dtos.input.auth.create.VerifyUserInputDto import VerifyUserInputDto
from src.application.usecases.auth.VerifyUserUseCase import VerifyUserUseCase
from src.controllers.auth import namespace
from src.application.schemas.auth.LoginSchemas import LoginSchemas, api
from src.application.schemas.common.ErrorSchemas import ErrorSchemas
from src.infra.utils.handlers.ErrorHandler import ErrorHandler


class LoginResource(Resource):
    @namespace.doc('Endpoint de criação de usuário')
    @namespace.expect(LoginSchemas.login_user_schema())
    @namespace.response(200, 'Ok', LoginSchemas.login_user_response())
    @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
    @namespace.response(401, 'Unauthorized', ErrorSchemas.http_401())
    @namespace.response(403, 'Forbidden', ErrorSchemas.http_403())
    @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
    @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
    @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
    @ErrorHandler.handle_exceptions
    def post(self) -> Response:
        data = request.json

        input_dto = VerifyUserInputDto()
        input_dto.set_attributes(**data)

        usecase: VerifyUserUseCase = current_app.usecases.verify_user_usecase
        output_dto = usecase.execute(input_dto=input_dto)

        login_user(output_dto.user_entity)

        return self.make_success_response(id=output_dto.user_entity.id)

    def make_success_response(self, id: UUID) -> Response:
        response_data = {
                'id': str(id),
                'success': True,
                'message': 'Usuário logado com sucesso.',
                'statuscode': 200}
        response = make_response(response_data, 200)
        response.headers['Content-Type'] = 'application/json'
        return response
