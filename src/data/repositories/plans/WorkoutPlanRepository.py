from sqlalchemy.orm import Session
from src.application.contracts.data.repositories.plans.IWorkoutPlanRepository import IWorkoutPlanRepository
from src.domain.entities.plans.WorkoutPlanEntity import WorkoutPlanEntity


class WorkoutPlanRepository(IWorkoutPlanRepository):
    def __init__(self, session: Session):
        super().__init__(session, WorkoutPlanEntity)
