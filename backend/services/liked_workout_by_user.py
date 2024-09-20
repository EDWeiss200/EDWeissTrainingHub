from utils.repository import AbstractRepository
from schemas.schemas import WorkoutMostLiked
from fastapi import HTTPException


class LikedWorkoutService:
    
    def __init__(self,lk_repo: AbstractRepository):
        self.lk_repo = lk_repo()

    async def like_workout(self,user_id,workout_id):

        like_workout_add = {
            'user_id': user_id,
            'workout_id':workout_id
        }
        try:
            like_workout = await self.lk_repo.add_one_not_return(like_workout_add)
        except:
            raise HTTPException(status_code=403,detail="WORKOUT ALREADY LIKE")
        return like_workout
    
    async def most_liked_workout(self):

        column = "workout_id"
        workouts = await self.lk_repo.find_count(column,5)
        results = {}
        for w in workouts:
            results[w[0]] = w[1]

        results = dict(sorted(results.items(), key=lambda item: item[1],reverse=True))
        

        return results
