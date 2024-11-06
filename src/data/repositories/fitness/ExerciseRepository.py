from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.fitness.IExerciseRepository import IExerciseRepository
from src.domain.entities.fitness.ExerciseEntity import ExerciseEntity


class ExerciseRepository(IExerciseRepository):
    def __init__(self, session: Session):
        super().__init__(session, ExerciseEntity)
