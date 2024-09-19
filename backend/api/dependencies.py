from services.exercise import ExerciseService
from repositories.exercise import ExerciseRepository
from services.workout import WorkoutService
from repositories.workout import WorkoutRepository
from services.user import UserSercvice
from repositories.user import UserRepository
from repositories.liked_workout_by_user import LikedWorkoutRepository
from services.liked_workout_by_user import LikedWorkoutService

def exercise_service() -> ExerciseService:
    return ExerciseService(ExerciseRepository)

def workout_service() -> WorkoutService:
    return WorkoutService(WorkoutRepository)

def user_service() -> UserSercvice:
    return UserSercvice(UserRepository)

def likedworkout_service() -> LikedWorkoutService:
    return LikedWorkoutService(LikedWorkoutRepository)