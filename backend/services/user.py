from repositories.user import UserRepository
from utils.repository import AbstractRepository
from schemas.schemas import UserInfo

class UserSercvice:
    
    def __init__(self,user_repo: AbstractRepository):
        self.user_repo = user_repo()

    async def delete_one(self,user_id):
        user_delete_id = await self.user_repo.delete_one(user_id)
        return user_delete_id

    async def find_all(self):
        user_all = await self.user_repo.find_all()
        return user_all
    
    async def filter_by_direction(self,direction):
        filters = [self.user_repo.model.direction == direction]
        user_res = await self.user_repo.filter(filters)
        return user_res

    async def filter_by_gym_status(self,gym_status):
        filters = [self.user_repo.model.gym_status == gym_status]
        user_res = await self.user_repo.filter(filters)
        return user_res
