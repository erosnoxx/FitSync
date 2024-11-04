class NotFoundError(Exception):
    """Raised when a resource is not found."""

    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = f"Not Found: {message}"
        self.status_code = 404
 
    def __str__(self):
        return f"{self.status_code}: {self.message}"
