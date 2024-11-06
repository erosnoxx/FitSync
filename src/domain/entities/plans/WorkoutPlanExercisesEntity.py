from uuid import UUID
from src.domain.entities import (BaseEntity, db, schema)


class WorkoutPlanExercisesEntity(BaseEntity):
    __tablename__ = 'workout_plan_exercises'

    workout_plan_id = db.Column(db.ForeignKey(f'{schema}.workout_plans.id'), nullable=False)
    exercise_id = db.Column(db.ForeignKey(f'{schema}.exercises.id'), nullable=False)
    repetitions = db.Column(db.Integer, nullable=False, default=6)
    sets = db.Column(db.Integer, nullable=False, default=3)
    order = db.Column(db.Integer, nullable=False)

    exercise = db.relationship('ExerciseEntity', back_populates='workout_plan_exercises')
    workout_plan = db.relationship('WorkoutPlanEntity', back_populates='workout_plan_exercises')
    workout_execution = db.relationship(
        'WorkoutExecutionEntity',
        back_populates='workout_plan_exercises',
        uselist=True,
        cascade='all,delete-orphan')

    def __init__(self,
                workout_plan_id: UUID,
                exercise_id: UUID,
                order: int,
                repetitions: int=6,
                sets: int=3) -> None:
        self.set_workout_plan_id(workout_plan_id)
        self.set_exercise_id(exercise_id)
        self.set_order(order)
        self.set_repetitions(repetitions)
        self.set_sets(sets)

    def set_workout_plan_id(self, workout_plan_id: UUID) -> None:
        if not isinstance(workout_plan_id, UUID):
            raise TypeError('Workout Plan ID deve ser um UUID')
        if not workout_plan_id:
            raise ValueError('Workout Plan ID não pode ser vazio')
        self.workout_plan_id = workout_plan_id

    def set_exercise_id(self, exercise_id: UUID) -> None:
        if not isinstance(exercise_id, UUID):
            raise TypeError('Exercise ID deve ser um UUID')
        if not exercise_id:
            raise ValueError('Exercise ID não pode ser vazio')
        self.exercise_id = exercise_id

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

    def set_order(self, order: int) -> None:
        if not isinstance(order, int):
            raise TypeError('Ordem deve ser um número inteiro')
        if order <= 0:
            raise ValueError('Ordem deve ser maior que zero')
        self.order = order
