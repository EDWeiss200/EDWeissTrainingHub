from fastapi import APIRouter,Depends
from services.workout import WorkoutService
from schemas.schemas import WorkoutSchemaAdd
from .dependencies import workout_service
from auth.auth import current_user
from models.models import User

router = APIRouter(
    tags=["workout"],
    prefix="/workout"
)

@router.get("/all")
async def get_all_workout(

):
    pass

@router.post("/add")
async def add_one_workout(
    workout: WorkoutSchemaAdd,
    workout_service: WorkoutService = Depends(workout_service),
    user: User =  Depends(current_user)
):
    workout_id = await workout_service.add_workout(workout,user.id)
    return {"workout_id" : workout_id}
