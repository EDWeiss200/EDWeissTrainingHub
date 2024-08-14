from fastapi import APIRouter,Depends
from services.workout import WorkoutService
from schemas.schemas import WorkoutSchemaAdd,Direction
from .dependencies import workout_service
from auth.auth import current_user
from models.models import User
from fastapi_cache.decorator import cache
import time

router = APIRouter(
    tags=["workout"],
    prefix="/workout"
)



@router.post("/add")
async def add_one_workout(
    workout: WorkoutSchemaAdd,
    workout_service: WorkoutService = Depends(workout_service),
    user: User =  Depends(current_user)
):
    workout_id = await workout_service.add_workout(workout,user.id)
    return {"workout_id" : workout_id}

@router.delete("/del")
async def delete_one(
    id: int,
    workout_service: WorkoutService = Depends(workout_service),
    user:User = Depends(current_user)
):
    workout_id = await workout_service.delete_workout(id)
    return{"delete_workout" : workout_id}


@router.get("/all")
@cache(expire=30)
async def find_all(
    workout_service: WorkoutService = Depends(workout_service),
    user:User = Depends(current_user)
):
    workoyt_all = await workout_service.find_all()
    return workoyt_all

@router.get("/filter/direction")
@cache(expire=30)
async def find_by_direction(
    direction: Direction,
    workout_service: WorkoutService = Depends(workout_service),
    user: User = Depends(current_user)
):
    workout_find = await workout_service.filter_by_direction(direction)
    return workout_find


@router.get("/{id}")
async def get_workout(
    id: int,
    workout_service: WorkoutService = Depends(workout_service),
    user: User = Depends(current_user)
):
    workout = await workout_service.find_one_by_id(id)
    return workout
    