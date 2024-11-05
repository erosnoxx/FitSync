from src.application.schemas import *


class ErrorSchemas:
    @staticmethod
    def http_400() -> Model:
        return api.model('Error 400', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Requisição inválida. Verifique os dados enviados.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=400)
        })
    
    @staticmethod
    def http_404() -> Model:
        return api.model('Error 404', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Recurso não encontrado.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=404)
        })

    @staticmethod
    def http_500() -> Model:
        return api.model('Error 500', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Erro interno no servidor.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=500)
        })

    @staticmethod
    def http_409() -> Model:
        return api.model('Error 409', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Conflito nos dados enviados.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=409)
        })
    
    @staticmethod
    def http_403() -> Model:
        return api.model('Error 403', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Acesso negado.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=403)
        })
    
    @staticmethod
    def http_401() -> Model:
        return api.model('Error 401', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Acesso não autorizado.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=401)
        })
