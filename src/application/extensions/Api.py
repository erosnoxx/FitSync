from flask import Flask
from flask_restx import Api

api = Api(prefix='/api/v1/', doc='/api/v1/docs/')


class Api:
    routes_registered = False
    def __init__(self, app: Flask):
        api.init_app(app=app)
        if not self.routes_registered:
            api.add_namespace(app.controllers.auth_controller.namespace)
            self.routes_registered = True
