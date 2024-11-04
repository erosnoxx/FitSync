class InternalServerError(Exception):
    """Internal server error exception."""

    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = f"Internal Server Error: {message}"
        self.status_code = 500

    def __str__(self):
        return f"{self.status_code}: {self.message}"
    