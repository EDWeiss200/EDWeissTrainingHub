from utils.repository import AbstractRepository
from schemas.schemas import ExerciseSchemaAdd

class ExerciseService:
    def __init__(self,exercise_repo: AbstractRepository):
        self.exercise_repo: AbstractRepository = exercise_repo()

    async def add_exercise(self,exercise: ExerciseSchemaAdd,user_id):
        exercise_dict = exercise.model_dump()
        exercise_dict['author_id'] = user_id
        exercise_id = await self.exercise_repo.add_one(exercise_dict)
        return exercise_id