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



@router.post("/add")
async def add_one_exercise(
    exercise : ExerciseSchemaAdd,
    exercise_service : ExerciseService = Depends(exercise_service),
    user: User = Depends(current_user)
):
    exercise_id = await exercise_service.add_exercise(exercise,user.id)
    return {"exercise_id" : exercise_id}
    
@router.delete("/del")
async def delete_one(
    id: int,
    exercise_service: ExerciseService = Depends(exercise_service),
    user: User = Depends(current_user)

):
    exercise_id = await exercise_service.delete_exercise(id)
    return {"delete_exercise": exercise_id}

@router.get("/all")
async def find_all(
    exercise_service:ExerciseService = Depends(exercise_service),
    user:User = Depends(current_user)
):
    exercise_all = await exercise_service.find_all()
    return exercise_all