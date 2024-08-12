from fastapi import APIRouter,Depends
from typing import Annotated
from repositories.exercise import ExerciseRepository
from schemas.schemas import ExerciseSchemaAdd
from repositories.exercise import ExerciseRepository
from services.exercise import ExerciseService
from .dependencies import exercise_service

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
    exercise_service : ExerciseService = Depends(exercise_service)
):
    exercise_id = await exercise_service.add_exercise(exercise)
    return {"exercise_id" : exercise_id}
    
