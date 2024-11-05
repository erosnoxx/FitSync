from typing import Dict

from src.application.dtos.input.common.BaseInputDto import BaseInputDto


class VerifyUserInputDto(BaseInputDto):
    def __init__(self,
                username: str=None,
                password: str=None) -> None:
        self.username = username
        self.password = password

    @property
    def requireds_fields(self) -> Dict[str, any]:
        return {
            "username": str,
            "password": str}
