from src.controllers.auth.AuthController import AuthController


class GlobalControllers:
    def __init__(self):
        self.auth_controller = AuthController()
