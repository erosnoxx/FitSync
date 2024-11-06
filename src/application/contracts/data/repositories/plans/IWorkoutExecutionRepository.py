from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.plans.WorkoutExecutionEntity import WorkoutExecutionEntity


class IWorkoutExecutionRepository(ABC, BaseRepository[WorkoutExecutionEntity]):
    pass
