from fastapi import APIRouter
from repositories.exercise import ExerciseRepository

router = APIRouter(
    tags=["workout"],
    prefix="/workout"
)

@router.get("/all")
async def get_all_workout(

):
    pass
