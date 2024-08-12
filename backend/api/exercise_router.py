from fastapi import APIRouter,Depends
from typing import Annotated
from repositories.exercise import ExerciseRepository
from schemas.schemas import ExerciseSchemaAdd
from repositories.exercise import ExerciseRepository

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

):
    exercise_dict = exercise.model_dump()
    exercise_id = await ExerciseRepository().add_one(exercise_dict)
    return {"exercise_id" : exercise_id}
    
