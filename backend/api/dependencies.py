from services.exercise import ExerciseService
from repositories.exercise import ExerciseRepository
from services.workout import WorkoutService
from repositories.workout import WorkoutRepository
from services.user import UserSercvice
from repositories.user import UserRepository

def exercise_service() -> ExerciseService:
    return ExerciseService(ExerciseRepository)

def workout_service() -> WorkoutService:
    return WorkoutService(WorkoutRepository)

def user_service() -> UserSercvice:
    return UserSercvice(UserRepository)