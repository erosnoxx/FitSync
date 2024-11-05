from src.application.schemas import *


class LogoutSchemas:
    @staticmethod
    def logout_user_response() -> Model:
        return api.model('Schema de resposta para logout de usuário', {
            'success':  fields.Boolean(required=True, default='Indicação de sucesso da operação'),
            'message':  fields.String(required=False, default='Mensagem de resposta'),
            'statuscode':  fields.Integer(required=True, description='Código de status da resposta', default=200)
        })
