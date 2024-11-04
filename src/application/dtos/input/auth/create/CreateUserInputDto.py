from typing import Dict
from src.application.dtos.input.common.BaseInputDto import BaseInputDto


class CreateUserInputDto(BaseInputDto):
    def __init__(self,
                username: str=None,
                email: str=None,
                password: str=None) -> None:
        self.username = username.lower()
        self.email = email
        self.password = password
    
    @property
    def requireds_fields(self) -> Dict[str, any]:
        return {
            "username": str,
            "email": str,
            "password": str}
