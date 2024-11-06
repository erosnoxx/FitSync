from datetime import date
from uuid import UUID
from src.domain.entities import (BaseEntity, db, schema)


class PersonEntity(BaseEntity):
    __tablename__ = 'persons'

    user_id = db.Column(db.ForeignKey(f'{schema}.users.id'), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(11), nullable=True)
    avatar_url = db.Column(db.String(255), unique=True, nullable=True)

    user = db.relationship('UserEntity', back_populates='person')

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    @property
    def full_name(self) -> str:
        return  f'{self.first_name} {self.last_name}'
    
    def __init__(self,
                user_id: UUID,
                first_name: str,
                last_name: str,
                birthdate: date,
                phone_number: str=None,
                avatar_url: str=None) -> None:
        self.set_user_id(user_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_birthdate(birthdate)
        self.set_phone_number(phone_number)
        self.set_avatar_url(avatar_url)

    def set_user_id(self, user_id: UUID) -> None:
        if not isinstance(user_id, UUID):
            raise ValueError('user_id deve ser um UUID')
        if not user_id:
            raise ValueError('user_id não pode ser vazio')
        
        self.user_id = user_id

    def set_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise TypeError('First name deve ser uma string')
        if not first_name:
            raise ValueError('First name não pode ser vazio')
        if len(first_name) > 50:
            raise ValueError('Primeiro nome deve ter no máximo 50 caracteres')
        if len(first_name) <= 1:
            raise  ValueError('Primeiro nome deve ter no mínimo 2 caracteres')
        if not first_name.isalnum():
            raise ValueError('Primeiro nome deve conter apenas letras')
        
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            raise TypeError('Last name deve ser uma string')
        if not last_name:
            raise ValueError('Last name não pode ser vazio')
        if len(last_name) > 50:
            raise ValueError('Último nome deve ter no máximo 50 caracteres')
        if len(last_name) <= 1:
            raise ValueError('Último nome deve ter no mínimo 2 caracteres')
        if not last_name.isalnum():
            raise ValueError('Último nome deve conter apenas letras')
        
        self.last_name = last_name

    def set_birthdate(self, birthdate: date) -> None:
        if not isinstance(birthdate, date):
            raise TypeError('birthdate deve ser uma instância de date')
        if birthdate > date.today():
            raise ValueError('birthdate não pode ser uma data futura')
        
        self.birthdate = birthdate

    def set_phone_number(self, phone_number: str) -> None:
        if phone_number and not phone_number.isdigit():
            raise ValueError('phone_number deve conter apenas dígitos')
        if phone_number and len(phone_number) != 11:
            raise ValueError('phone_number deve ter exatamente 11 dígitos')
        
        self.phone_number = phone_number

    def set_avatar_url(self, avatar_url: str) -> None:
        if avatar_url and len(avatar_url) > 255:
            raise ValueError('avatar_url não pode ter mais de 255 caracteres')
        if avatar_url and not '.' in avatar_url:
            raise ValueError('avatar_url deve conter um ponto')
        
        self.avatar_url = avatar_url
