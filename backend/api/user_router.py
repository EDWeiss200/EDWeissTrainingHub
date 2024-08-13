from fastapi import APIRouter,Depends
from repositories.user import UserRepository
from .dependencies import user_service
from services.user import UserSercvice
from auth.auth import current_user
from models.models import User
from schemas.schemas import Direction,GymStatus


router = APIRouter(
    tags=["user"],
    prefix="/user"
)


@router.delete("/del")
async def delete_one(
    id: int,
    user_service : UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_id = await user_service.delete_one(id)
    return {"delete_user": user_id}

@router.get("/all")
async def find_all(
    user_service:UserSercvice = Depends(user_service),
    user:User = Depends(current_user)
):
    user_all = await user_service.find_all()
    return user_all

@router.get("/filter/direction")
async def find_all(
    direction: Direction,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_direction(direction)
    return user_res

@router.get("/filter/gym_status")
async def find_all(
    gym_status: GymStatus,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_gym_status(gym_status)
    return user_res


