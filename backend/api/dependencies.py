from services.exercise import ExerciseService
from repositories.exercise import ExerciseRepository


def exercise_service() -> ExerciseService:
    return ExerciseService(ExerciseRepository)