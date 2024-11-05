from src.application.schemas import *


class LoginSchemas:
    @staticmethod
    def login_user_schema() -> Model:
        return api.model('Schema para login de usuário', {
            'username': fields.String(required=True, description='Nome de usuário'),
            'password': fields.String(required=True, description='Senha do usuário'),
        })

    @staticmethod
    def login_user_response() -> Model:
        return api.model('Schema de resposta para login de usuário', {
            'id': fields.Integer(required=True, description='ID do usuário'),
            'success':  fields.Boolean(required=True, default='Indicação de sucesso da operação'),
            'message':  fields.String(required=False, default='Mensagem de resposta'),
            'statuscode':  fields.Integer(required=True, description='Código de status da resposta', default=200)
        })
