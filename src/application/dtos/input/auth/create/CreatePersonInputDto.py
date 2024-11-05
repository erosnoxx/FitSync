from datetime import date
from uuid import UUID
from typing import Dict
from src.application.dtos.input.common.BaseInputDto import BaseInputDto


class CreatePersonInputDto(BaseInputDto):
    def __init__(self,
                 user_id: UUID=None,
                 first_name: str=None,
                 last_name: str=None,
                 birthdate: str=None,
                 phone_number: str = None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.phone_number = phone_number
    
    @property
    @staticmethod
    def required_fields(self) -> Dict[str, type]:
        return {
            "user_id": UUID,
            "first_name": str,
            "last_name": str,
            "birthdate": str,
        }
