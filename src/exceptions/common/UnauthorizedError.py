class UnauthorizedError(Exception):
    """Raised when the user is not authorized to perform an action."""

    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = f"Unauthorized: {message}"
        self.status_code = 401

    def __str__(self):
        return f"{self.status_code}: {self.message}"
