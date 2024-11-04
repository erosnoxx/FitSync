from datetime import datetime, timezone
from flask_login import UserMixin
from src.domain.entities import (BaseEntity, db)


class UserEntity(BaseEntity, UserMixin):
    __tablename__ = 'users'

    username = db.Column(db.String(10), unique=True,  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=True)
    is_enabled = db.Column(db.Boolean, nullable=False, default=True)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    person = db.relationship('PersonEntity', back_populates='user', uselist=False)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return self.is_enabled
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self,
                username: str,
                email: str,
                password_hash: str,
                is_verified: bool=True,
                is_enabled: bool=True,
                last_login: datetime=None) -> None:
        self.set_username(username)
        self.set_email(email)
        self.set_password(password_hash)
        self.is_verified = is_verified
        self.is_enabled = is_enabled
        self.last_login = last_login if last_login else datetime.now(timezone.utc)

    def set_username(self, username: str) -> None:
        if  not username:
            raise ValueError('Username não pode ser vazio')
        if  len(username) > 10:
            raise ValueError('Username não pode ter mais de 50 caracteres')
        if len(username) < 3:
            raise ValueError('Username deve ter pelo menos 3 caracteres')

        self.username = username

    def set_email(self, email: str) -> None:
        if not email:
            raise ValueError('E-mail não pode ser vazio')
        if  len(email) > 100:
            raise ValueError('E-mail não pode ter mais de 100 caracteres')
        if  len(email) < 5:
            raise ValueError('E-mail deve ter pelo menos 5 caracteres')
        if  '@' not in email:
            raise ValueError('E-mail deve conter "@"')
        if   '.' not in email:
            raise ValueError('E-mail deve conter "."')
        
        self.email = email
    
    def set_password(self, password_hash: str) -> None:
        if not password_hash:
            raise ValueError('Senha não pode ser vazia')
        if len(password_hash) > 255:
            raise ValueError('Senha não pode ter mais de 255 caracteres')
        if len(password_hash) < 8:
            raise ValueError('Senha deve ter pelo menos 8 caracteres')

        self.password_hash = password_hash
