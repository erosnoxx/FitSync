from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.fitness.ExerciseEntity import ExerciseEntity


class IExerciseRepository(ABC, BaseRepository[ExerciseEntity]):
    pass
