from pydantic import BaseModel,EmailStr
from enum import Enum
from typing import Optional

class Item(BaseModel):
    name:str


class GymStatus(str, Enum):
    beginner = "beginner"
    dystrophic = "dystrophic"
    amateur = "amateur"
    experienced = "experienced"
    master = "master"
    Gigachad = "Gigachad"
    UltraGigachad = "UltraGigaChad"

class Direction(str, Enum):
    workout = "workout"
    powerlifting = "powerlifting"
    crossfit = "crossfit"
    sucker = "sucker"
    drochila = "drochila"
    Gigachad = "Gigachad"


class Gender(str, Enum):
    men = "men"
    women = "women"


class Muscle_Group(str, Enum):
    Back_muscles = "Back muscles"
    Pectoral_muscles = "Pectoral muscles"
    Biceps = "Biceps"
    Triceps = "Triceps"
    Quadriceps = "Quadriceps"
    Trapezoidal_muscles  = "Trapezoidal muscles"
    Calf_muscles = "Calf muscles"
    Forearms =  "Forearms"
    Press = "Press"
    The_widest_muscles = "The widest muscles"
    Deltoid_muscles =  "Deltoid muscles"
    Gluteal_muscles = "Gluteal muscles"


class UserInfo(BaseModel):
    id : int
    username : str
    email : EmailStr
    gender : Gender
    weight : int
    height : int 
    direction : Direction
    gym_status : GymStatus
    count_workout: int


    class Config:
        from_attributes = True

class UserInfoRelationship(UserInfo):
    workout_liked: list["WorkoutLikedSchema"]

    class Config:
        from_attributes = True


class ExerciseSchema(BaseModel):
    id : int
    author_id : int
    name : str
    muscle_group : Muscle_Group
    number_of_repetitions : int
    number_of_approaches : int
    break_between_approaches : int
    workload : int

    class Config:
        from_attributes = True

class WorkoutLikedSchema(BaseModel):
    id: int
    name: str

class ExerciseSchemaAdd(BaseModel):
    name : str
    muscle_group : Muscle_Group
    number_of_repetitions : int
    number_of_approaches : int
    break_between_approaches : int
    workload : int

class WorkoutSchema(BaseModel):
    id : int
    author_id : int
    name : str
    break_between_exercises : int
    direction : Direction
    exercise_1id : int
    exercise_2id : Optional[int] | None
    exercise_3id : Optional[int] | None
    exercise_4id : Optional[int] | None
    exercise_5id : Optional[int] | None


    class Config:
        from_attributes = True
    
class WorkoutSchemaAdd(BaseModel):
    name : str
    break_between_exercises : int
    direction : Direction
    exercise_1id : int
    exercise_2id: Optional[int] | None
    exercise_3id: Optional[int] | None
    exercise_4id: Optional[int] | None
    exercise_5id: Optional[int] | None


