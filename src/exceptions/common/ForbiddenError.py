class ForbiddenError(Exception):
    """Exception raised for conflicts between two or more objects."""

    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = f"Forbidden: {message}"
        self.status_code = 403

    def __str__(self):
        return f"{self.status_code}: {self.message}"
