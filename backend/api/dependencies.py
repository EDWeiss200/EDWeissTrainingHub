from services.exercise import ExerciseService
from repositories.exercise import ExerciseRepository
from services.workout import WorkoutService
from repositories.workout import WorkoutRepository


def exercise_service() -> ExerciseService:
    return ExerciseService(ExerciseRepository)

def workout_service() -> WorkoutService:
    return WorkoutService(WorkoutRepository)