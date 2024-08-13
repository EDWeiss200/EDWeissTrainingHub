import uuid
from pydantic import EmailStr
from typing import Optional
from fastapi_users import schemas
from schemas.schemas import Gender,GymStatus,Direction

class UserRead(schemas.BaseUser[int]):
    id: int 
    email: EmailStr
    username : str
    gender : Gender
    weight : int 
    height : int
    direction : Direction
    gym_status : GymStatus
    count_workout: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


    class Config:
        from_attributes = True



class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    username : str
    gender : Gender
    weight : int 
    height : int
    direction : Direction
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass