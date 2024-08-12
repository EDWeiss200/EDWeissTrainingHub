from utils.repository import AbstractRepository
from schemas.schemas import WorkoutSchemaAdd,WorkoutSchema

class WorkoutService:
    def __init__(self,workout_repo: AbstractRepository):
        self.workout_repo: AbstractRepository = workout_repo()

    async def add_workout(self,workout: WorkoutSchemaAdd,user_id):
        workout_dict = workout.model_dump()
        workout_dict["author_id"] = user_id
        for i in workout_dict:
            if workout_dict[i] == 0 and i!="direction" and i!="exercise_id1":
                workout_dict[i] = None
        workout_id = await self.workout_repo.add_one(workout_dict)
        return workout_id