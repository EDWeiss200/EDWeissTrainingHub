from repositories.user import UserRepository
from utils.repository import AbstractRepository
from schemas.schemas import UserInfo

class UserSercvice:
    """
    beginner = "beginner"
    dystrophic = "dystrophic"
    amateur = "amateur"
    experienced = "experienced"
    master = "master"
    Gigachad = "Gigachad"
    UltraGigachad = "UltraGigachad"

    """
    

    gym_status = {
        5: "dystrophic",
        20: "amateur",
        50:"experienced",
        100:"master",
        200:"Gigachad",
        500:"UltraGigaChad"
    }
    
    def __init__(self,user_repo: AbstractRepository):
        self.user_repo = user_repo()

    async def delete_one(self,user_id):
        user_delete_id = await self.user_repo.delete_one(user_id)

        return user_delete_id

    async def find_all(self):
        user_all = await self.user_repo.find_all()
        return user_all
    
    async def find_one_by_id(self,id):
        filters = [self.user_repo.model.id == id]
        user = await self.user_repo.filter(filters)
        return user
    
    async def filter_by_direction(self,direction):
        filters = [self.user_repo.model.direction == direction]
        user_res = await self.user_repo.filter(filters)
        return user_res

    async def filter_by_gym_status(self,gym_status):
        filters = [self.user_repo.model.gym_status == gym_status]
        user_res = await self.user_repo.filter(filters)
        return user_res
    
    async def completing_workout(self,user_id):
        user = await self.find_one_by_id(user_id)
        user_dict = user[0].model_dump()
        count_workout = user_dict['count_workout']
        
        status = "beginner"
        for i in self.gym_status:
            if count_workout+1 >= i:
                status = self.gym_status[i]

        values_up = {
            'count_workout' : count_workout+1,
            'gym_status' : status
        }

        values_base = {
            'count_workout' : count_workout+1
        }
            
        
        if status == user_dict['gym_status']:
            user_id = await self.user_repo.update(user_id,values_base)
        else:
            user_id = await self.user_repo.update(user_id,values_up)
            

        return user_id,count_workout+1,status