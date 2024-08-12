from fastapi import APIRouter,Depends
from typing import Annotated
from repositories.exercise import ExerciseRepository
from schemas.schemas import ExerciseSchemaAdd
from repositories.exercise import ExerciseRepository
from services.exercise import ExerciseService
from .dependencies import exercise_service
from auth.auth import current_user
from auth.database import User

router = APIRouter(
    tags=["exercise"],
    prefix="/exercise"
)

@router.get("/all")
async def get_all_exercise(

):
    pass

@router.post("/add")
async def add_one_exercise(
    exercise : ExerciseSchemaAdd,
    exercise_service : ExerciseService = Depends(exercise_service),
    user: User = Depends(current_user)
):
    exercise_id = await exercise_service.add_exercise(exercise,user.id)
    return {"exercise_id" : exercise_id}
    
