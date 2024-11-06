from uuid import UUID
from src.domain.entities import (BaseEntity, db, schema)


class WorkoutPlanEntity(BaseEntity):
    __tablename__ = 'workout_plans'

    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.ForeignKey(f'{schema}.users.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.Integer, nullable=False, default=1)
    estimed_duration = db.Column(db.Integer, nullable=False)

    user = db.relationship('UserEntity', back_populates='workout_plans')
    workout_plan_exercises = db.relationship(
        'WorkoutPlanExercisesEntity',
        back_populates='workout_plan',
        uselist=True,
        cascade='all,delete-orphan')

    def __init__(self,
                name: str,
                user_id: UUID,
                description: str,
                estimed_duration: int,
                difficulty: int=1) -> None:
        self.set_name(name)
        self.set_user_id(user_id)
        self.set_description(description)
        self.set_estimed_duration(estimed_duration)
        self.set_difficulty(difficulty)

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Name deve ser uma string')
        if not name:
            raise ValueError('Name não pode ser vazio')
        if len(name) > 50:
            raise ValueError('Name não pode ter mais de 50 caracteres')
        if len(name) < 2:
            raise ValueError('Name deve ter pelo menos 2 caracteres')
        
        self.name = name

    def set_user_id(self, user_id: UUID) -> None:
        if not isinstance(user_id, UUID):
            raise TypeError('User ID deve ser um UUID')
        if not user_id:
            raise ValueError('User ID não pode ser vazio')
        
        self.user_id = user_id

    def set_description(self, description: str) -> None:
        if description and len(description) > 500:
            raise ValueError('Descrição não pode ter mais de 500 caracteres')
        self.description = description

    def set_difficulty(self, difficulty: int) -> None:
        if not isinstance(difficulty, int):
            raise TypeError('Difficulty deve ser um número inteiro')
        if difficulty < 1 or difficulty > 10:
            raise ValueError('Difficulty deve estar entre 1 e 10')
        self.difficulty = difficulty

    def set_estimed_duration(self, estimed_duration: int) -> None:
        if not isinstance(estimed_duration, int):
            raise TypeError('Duração estimada deve ser um número inteiro')
        if estimed_duration <= 0:
            raise ValueError('Duração estimada deve ser maior que zero')
        self.estimed_duration = estimed_duration
