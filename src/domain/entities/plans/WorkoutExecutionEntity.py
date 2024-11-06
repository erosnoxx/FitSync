from uuid import UUID
from src.domain.entities import (BaseEntity, db, schema)


class WorkoutExecutionEntity(BaseEntity):
    __tablename__ = "workout_execution"

    workout_plan_exercise_id = db.Column(db.ForeignKey(f'{schema}.workout_plan_exercises.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Boolean, nullable=False)

    workout_plan_exercises = db.relationship('WorkoutPlanExercisesEntity', back_populates='workout_execution')

    def __init__(self,
                workout_plan_exercise_id: UUID,
                date: str,
                repetitions: int,
                sets: int,
                weight: int,
                progress: bool) -> None:
        self.set_workout_plan_exercise_id(workout_plan_exercise_id)
        self.set_date(date)
        self.set_repetitions(repetitions)
        self.set_sets(sets)
        self.set_weight(weight)
        self.set_progress(progress)

    def set_workout_plan_exercise_id(self, workout_plan_exercise_id: UUID) -> None:
        if not isinstance(workout_plan_exercise_id, UUID):
            raise TypeError('Workout Plan Exercise ID deve ser um UUID')
        self.workout_plan_exercise_id = workout_plan_exercise_id

    def set_date(self, date: str) -> None:
        if not isinstance(date, str):
            raise TypeError('Data deve ser uma string no formato "YYYY-MM-DD"')
        try:
            self.date = date
        except ValueError:
            raise ValueError('Data deve ter o formato correto "YYYY-MM-DD"')

    def set_repetitions(self, repetitions: int) -> None:
        if not isinstance(repetitions, int):
            raise TypeError('Repetições deve ser um número inteiro')
        if repetitions <= 0:
            raise ValueError('Repetições deve ser maior que zero')
        self.repetitions = repetitions

    def set_sets(self, sets: int) -> None:
        if not isinstance(sets, int):
            raise TypeError('Séries deve ser um número inteiro')
        if sets <= 0:
            raise ValueError('Séries deve ser maior que zero')
        self.sets = sets

    def set_weight(self, weight: int) -> None:
        if not isinstance(weight, int):
            raise TypeError('Peso deve ser um número inteiro')
        if weight < 0:
            raise ValueError('Peso não pode ser negativo')
        self.weight = weight

    def set_progress(self, progress: bool) -> None:
        if not isinstance(progress, bool):
            raise TypeError('Progressão deve ser um valor booleano')
        self.progress = progress
