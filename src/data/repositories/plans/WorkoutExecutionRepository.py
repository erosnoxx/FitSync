from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.plans.IWorkoutExecutionRepository import IWorkoutExecutionRepository
from src.domain.entities.plans.WorkoutExecutionEntity import WorkoutExecutionEntity


class WorkoutExecutionRepository(IWorkoutExecutionRepository):
    def __init__(self, session: Session):
        super().__init__(session, WorkoutExecutionEntity)
