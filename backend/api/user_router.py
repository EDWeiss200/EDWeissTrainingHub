from fastapi import APIRouter
from repositories.user import UserRepository

router = APIRouter(
    tags=["user"],
    prefix="/user"
)

@router.get("/all")
async def get_all_user(

):
    pass