from flask import Response, make_response
from flask_restx import Resource
from src.exceptions.common import *
from src.exceptions.common.ForbiddenError import ForbiddenError


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
                return ErrorHandler.make_error_response(message=str(br), status_code=400)
            except UnauthorizedError as u:
                return ErrorHandler.make_error_response(message=str(u), status_code=401)
            except ForbiddenError as f:
                return ErrorHandler.make_error_response(message=str(f), status_code=403)
            except NotFoundError as nf:
                return ErrorHandler.make_error_response(message=str(nf), status_code=404)
            except ConflictError as c:
                return ErrorHandler.make_error_response(message=str(c), status_code=409)
            except InternalServerError as ise:
                return ErrorHandler.make_error_response(message=str(ise), status_code=500)
        return wrapper
