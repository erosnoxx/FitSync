from flask import Flask, make_response
from flask_login import LoginManager
from src.domain.entities.auth.UserEntity import UserEntity

lm = LoginManager()


class AuthManager:
    def __init__(self, app: Flask):
        lm.init_app(app=app)

        @lm.unauthorized_handler
        def unauthorized_callback():
            response_data = {
                'success': False,
                'statuscode': 401,
                'message': 'Você precisa estar autenticado para acessar esse recurso.'
            }
            response = make_response(response_data, 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        @lm.user_loader
        def load_user(user_id):
            return UserEntity.query.get(user_id)
