class BadRequestError(Exception):
    """Raised when the request is invalid or malformed."""
    
    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = f"Bad Request: {message}"
        self.status_code = 400

    def __str__(self):
        return f"{self.status_code}: {self.message}"
