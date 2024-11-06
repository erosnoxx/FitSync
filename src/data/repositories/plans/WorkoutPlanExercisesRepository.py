from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.plans.IWorkoutPlanExercisesRepository import IWorkoutPlanExercisesRepository
from src.domain.entities.plans.WorkoutPlanExercisesEntity import WorkoutPlanExercisesEntity


class WorkoutPlanExercisesRepository(IWorkoutPlanExercisesRepository):
    def __init__(self, session: Session):
        super().__init__(session, WorkoutPlanExercisesEntity)
