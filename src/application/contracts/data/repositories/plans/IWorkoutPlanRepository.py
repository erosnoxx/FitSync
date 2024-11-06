from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.plans.WorkoutPlanEntity import WorkoutPlanEntity


class IWorkoutPlanRepository(ABC, BaseRepository[WorkoutPlanEntity]):
    pass
