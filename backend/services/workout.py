from utils.repository import AbstractRepository
from schemas.schemas import WorkoutSchemaAdd,WorkoutSchema,WorkoutInfoRelationship


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
    
    async def delete_workout(self,workout_id):
        workout_delete_id = await self.workout_repo.delete_one(workout_id)
        return workout_delete_id
        
    async def find_all(self):
        workout_all = await self.workout_repo.find_all()
        return workout_all
    
    async def find_one_by_id(self,id):
        filters = [self.workout_repo.model.id == id]
        workout = await self.workout_repo.filter(filters)
        return workout
    
    async def filter_by_direction(self,direction):
        filters = [self.workout_repo.model.direction == direction]
        workout_res = await self.workout_repo.filter(filters)
        return workout_res

    async def find_liked_users(self,workout_id):
        
        relation_ship = self.workout_repo.model.user_liked
        users_all = await self.workout_repo.relationship_base_find(relation_ship,workout_id)
        result = [WorkoutInfoRelationship.model_validate(row,from_attributes=True) for row in users_all]

        for i in result[0]:
            if i[0] == 'user_liked':
                return i[1]

    async def find_liked_users_count(self,workout_id):
        
        relation_ship = self.workout_repo.model.user_liked
        users_all = await self.workout_repo.relationship_base_find(relation_ship,workout_id)
        result = [WorkoutInfoRelationship.model_validate(row,from_attributes=True) for row in users_all]

        count = 0
        print(result[0])
        for i in result[0]:
            if i[0] == 'user_liked':
                print(i)
                for j in i[1]:
                    count+=1

        return count

    async def most_liked_workout(self,workouts: dict) -> list:

        results=[]

        for i in workouts:
            workout = await self.find_one_by_id(i)
            workout_dict = workout[0].model_dump()
            workout_dict['count_likes'] = workouts[i]
            results.append(workout_dict)
        
        return results
