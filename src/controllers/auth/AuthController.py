from src.controllers.auth import namespace
from src.controllers.auth.resources.LoginResource import LoginResource
from src.controllers.auth.resources.LogoutResource import LogoutResource
from src.controllers.auth.resources.RegisterResource import RegisterResource



class AuthController:
    def __init__(self):
        self.namespace = namespace
        self.register_routes()
    
    def register_routes(self) -> None:
        self.namespace.add_resource(RegisterResource, '/users/register/')
        self.namespace.add_resource(LoginResource, '/users/login/')
        self.namespace.add_resource(LogoutResource, '/users/logout/')
