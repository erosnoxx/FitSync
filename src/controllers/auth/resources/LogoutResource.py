from src.application.schemas.auth.LogoutSchemas import LogoutSchemas
from src.application.schemas.common.ErrorSchemas import ErrorSchemas
from src.controllers.auth import namespace
from flask import make_response
from flask_login import login_required, logout_user, current_user
from flask_restx import Resource


class LogoutResource(Resource):
    @login_required
    @namespace.doc('Desloga o usuário.')
    @namespace.response(200, 'Ok', LogoutSchemas.logout_user_response())
    @namespace.response(401, 'Unauthorized', ErrorSchemas.http_401())
    def delete(self) -> None:
        if not current_user.is_authenticated:
            response_data = {
                'success': False,
                'statuscode': 401,
                'message': 'Usuário não está autenticado.'
            }
            response = make_response(response_data, 401)

            response.headers['Content-Type'] = 'application/json'
            return response

        id = current_user.id
        logout_user()
        
        response_data = {
            'success': True,
            'statuscode': 200,
            'message': 'Usuário deslogado com sucesso.',
            'id': id
        }
        response = make_response(response_data, 200)

        return response