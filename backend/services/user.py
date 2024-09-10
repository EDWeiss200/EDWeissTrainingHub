from repositories.user import UserRepository
from utils.repository import AbstractRepository
from schemas.schemas import UserInfo,UserInfoRelationship,WorkoutLikedSchema
from tasks.tasks import send_email_up_gymstatus,send_email_user_info
from fastapi import BackgroundTasks, HTTPException
from random import randint
from tasks.tasks import send_verification_code,send_changepass_code
from config import SECRET_JWT,ALGORITHM_JWT
import jwt
from  models.models import User,Workout
from auth.auth import password_helper




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

        users_all = await self.user_repo.find_all()
        return users_all
    
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
    
    async def completing_workout(self,user_id,user_verified):
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
            
        tasks = ''
        if status == user_dict['gym_status']:
            user_id = await self.user_repo.update(user_id,values_base)
        else:
            user_id = await self.user_repo.update(user_id,values_up)
            if user_verified:
                tasks = BackgroundTasks()
                tasks.add_task(send_email_up_gymstatus, user_dict['username'], user_dict["email"], status)
            
            

        return  {"user": user_id,'new_gym_status': status,'count_workout': count_workout+1} ,tasks


    async def get_user_info_by_email(self,user_id):
        user = await self.find_one_by_id(user_id)
        user_dict = user[0].model_dump()

        tasks = BackgroundTasks()
        tasks.add_task(send_email_user_info, user_dict['username'], user_dict["email"], user_dict)

        return {"status": 200},tasks
    

    async def verification_user_get_token(self,user_id,email):
        
        verification_code = randint(100000,999999)

        payload= {
            'key': verification_code,
            'id' : user_id
        }
        token = jwt.encode(payload, SECRET_JWT, algorithm=ALGORITHM_JWT)
        send_verification_code(email,verification_code)
        return token
    

    async def verification_user(self,key,token,id):
        try:
            decoded_token = jwt.decode(token, SECRET_JWT, algorithms=[ALGORITHM_JWT])
            token = decoded_token
        except:
            return HTTPException(status_code=400,detail='BAD_REQUEST')

        if id == token["id"] and token['key'] == key:
            filter = [self.user_repo.model.id == token['id']]
            values = {"is_verified" : True}

            user_id = await self.user_repo.update_by_filter(filter,values)

            return {"user" : user_id, "verified" : True}
        
        else: 
            return HTTPException(status_code=400,detail='BAD_DATA')


    async def get_token_to_changepass_by_email(self,email):

        filters = [self.user_repo.model.email == email]

        user = await self.user_repo.filter(filters)
        user_dict = user[0].model_dump()

        if user:
            changepass_code = randint(100000,999999)

            payload= {
                'key': changepass_code,
                'user_id': user_dict['id']
            }

            token = jwt.encode(payload, SECRET_JWT, algorithm=ALGORITHM_JWT)
            send_changepass_code(email,changepass_code)
            return token
        
        else:
            return HTTPException(status_code=400,detail='UNIDENTIFIED EMAIL')
            
        
    async def changepass_by_email_user(self,key,token,password):
            try:
                decoded_token = jwt.decode(token, SECRET_JWT, algorithms=[ALGORITHM_JWT])
                token = decoded_token
            except:
                return HTTPException(status_code=400,detail='BAD_REQUEST')

            if key == token['key']:

                hashed_password = password_helper.hash(password)

                filter = [self.user_repo.model.id == token['user_id']]
                values = {"hashed_password" : hashed_password}

                user_id = await self.user_repo.update_by_filter(filter,values)

                return {"user" : user_id, "new_password" : password}

            else:
                return HTTPException(status_code=401,detail='BAD_KEY')
    
    async def find_liked_workout(self,user_id):

        stmt = User.workout_liked
        loadOnly = Workout.id
        user_all = await self.user_repo.m2m_find_all(stmt,loadOnly,user_id)
        result = [UserInfoRelationship.model_validate(row,from_attributes=True) for row in user_all]
        for i in result[0]:
            if i[0] == 'workout_liked':
                return i[1]
