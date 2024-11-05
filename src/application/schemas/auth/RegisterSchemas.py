from src.application.schemas import *


class RegisterSchemas:
    @staticmethod
    def register_user_schema() -> Model:
        return api.model('Schema para criação de usuário', {
            'username': fields.String(required=True, description='Nome de usuário'),
            'email': fields.String(
                required=True,
                description='Endereço de e-mail do usuário.'),
            'password': fields.String(required=True, description='Senha do usuário'),
            'first_name': fields.String(required=True, description='Primeiro nome do usuário'),
            'last_name': fields.String(required=True, description='Último nome do usuário'),
            'birthdate': fields.Date(required=False, description='Data de nascimento do usuário (formato YYYY-MM-DD)'),
            'phone_number': fields.String(required=False, description='Número de telefone do usuário (formato XX9XXXXXXXX)'),
        })

    @staticmethod
    def register_user_response() -> Model:
        return api.model('Schema de resposta para criação de usuário', {
            'id': fields.Integer(required=True, description='ID do usuário'),
            'success':  fields.Boolean(required=True, default='Indicação de sucesso da operação'),
            'message':  fields.String(required=False, default='Mensagem de resposta'),
            'statuscode':  fields.Integer(required=True, description='Código de status da resposta', default=201)
        })
