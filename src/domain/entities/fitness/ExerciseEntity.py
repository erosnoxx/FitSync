from src.application.enums.fitness.EquipmentTypeEnum import EquipmentTypeEnum
from src.application.enums.fitness.ExerciseCategoryEnum import ExerciseCategoryEnum
from src.domain.entities import (BaseEntity, db)


class ExerciseEntity(BaseEntity):
    __tablename__ = "exercises"

    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.Enum(ExerciseCategoryEnum), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.Integer, nullable=False, default=1)
    equipament = db.Column(db.Enum(EquipmentTypeEnum), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    media_url = db.Column(db.String(255), nullable=True)

    workout_plan_exercises = db.relationship(
        'WorkoutPlanExercisesEntity',
        back_populates='exercise',
        uselist=True,
        cascade='all,delete-orphan')

    def __init__(self,
                name: str,
                category: ExerciseCategoryEnum,
                equipament: EquipmentTypeEnum,
                difficulty: int = 1,
                duration: int = None,
                description: str = None,
                media_url: str = None) -> None:
        self.set_name(name)
        self.set_category(category)
        self.set_equipament(equipament)
        self.set_difficulty(difficulty)
        self.set_duration(duration)
        self.set_description(description)
        self.set_media_url(media_url)

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

    def set_category(self, category: ExerciseCategoryEnum) -> None:
        if category not in ExerciseCategoryEnum:
            raise ValueError(f"Categoria inválida. Opções válidas: {[e.name for e in ExerciseCategoryEnum]}")
        self.category = category

    def set_equipament(self, equipament: EquipmentTypeEnum) -> None:
        if equipament not in EquipmentTypeEnum:
            raise ValueError(f"Equipamento inválido. Opções válidas: {[e.name for e in EquipmentTypeEnum]}")
        self.equipament = equipament

    def set_difficulty(self, difficulty: int) -> None:
        if not isinstance(difficulty, int):
            raise TypeError('Difficulty deve ser um número inteiro')
        if difficulty < 1 or difficulty > 10:
            raise ValueError('Difficulty deve estar entre 1 e 10')
        self.difficulty = difficulty

    def set_duration(self, duration: int) -> None:
        if duration is not None and (not isinstance(duration, int) or duration <= 0):
            raise ValueError('Duração deve ser um número inteiro positivo')
        self.duration = duration

    def set_description(self, description: str) -> None:
        if description and len(description) > 500:
            raise ValueError('Descrição não pode ter mais de 500 caracteres')
        self.description = description

    def set_media_url(self, media_url: str) -> None:
        if media_url and len(media_url) > 255:
            raise ValueError('URL da mídia não pode ter mais de 255 caracteres')
        if media_url and not media_url.startswith('http'):
            raise ValueError('URL da mídia deve começar com "http"')
        self.media_url = media_url
