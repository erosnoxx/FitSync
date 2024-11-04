from flask import Response, make_response
from flask_restx import Resource
from src.exceptions.common import *


class ErrorHandler:
    @staticmethod
    def make_error_response(message: str, status_code: int) -> Response:
        response_data = {
            'success': False,
            'statuscode': status_code,
            'message': message
        }
        response = make_response(response_data, status_code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def handle_exceptions(resource: Resource):
        def wrapper(*args, **kwargs):
            try:
                return resource(*args, **kwargs)
            except BadRequestError as br:
                return ErrorHandler.make_error_response(message=br)
            except ConflictError as c:
                return ErrorHandler.make_error_response(message=c)
            except NotFoundError as nf:
                return ErrorHandler.make_error_response(message=nf)
            except UnauthorizedError as u:
                return ErrorHandler.make_error_response(message=u)
            

            except InternalServerError as ise:
                return ErrorHandler.make_error_response(message=ise)
        return wrapper
