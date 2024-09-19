from utils.repository import AbstractRepository


class LikedWorkoutService:
    
    def __init__(self,lk_repo: AbstractRepository):
        self.lk_repo = lk_repo()

    async def like_workout(self,user_id,workout_id):

        like_workout_add = {
            'user_id': user_id,
            'workout_id':workout_id
        }
        like_workout = await self.lk_repo.add_one_not_return(like_workout_add)
        return like_workout
