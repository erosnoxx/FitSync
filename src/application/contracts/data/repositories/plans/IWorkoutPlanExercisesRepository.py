from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.plans.WorkoutPlanExercisesEntity import WorkoutPlanExercisesEntity


class IWorkoutPlanExercisesRepository(ABC, BaseRepository[WorkoutPlanExercisesEntity]):
    pass
