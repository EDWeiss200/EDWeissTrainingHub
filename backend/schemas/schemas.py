from pydantic import BaseModel,EmailStr
from enum import Enum

class Item(BaseModel):
    name:str


class GymStatus(Enum):
    beginner = "beginner"
    dystrophic = "dystrophic"
    amateur = "amateur"
    experienced = "experienced"
    master = "master"
    Gigachad = "Gigachad"
    UltraGigachad = "UltraGigachad"

class Direction(Enum):
    workout = "workout"
    powerlifting = "powerlifting"
    crossfit = "crossfit"
    sucker = "sucker"
    drochila = "drochila"
    Gigachad = "Gigachad"

class UserInfo(BaseModel):
    id : int
    username : str
    email : EmailStr
    gender : str
    weight : int
    height : int 
    direction : Direction
    gym_status : GymStatus
    days_of_training : int 
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

