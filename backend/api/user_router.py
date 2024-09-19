from fastapi import APIRouter,Depends,HTTPException,Response,Cookie,Request
from repositories.user import UserRepository
from .dependencies import user_service,likedworkout_service
from services.user import UserSercvice
from services.liked_workout_by_user import LikedWorkoutService
from auth.auth import current_user
from models.models import User
from schemas.schemas import Direction,GymStatus
from fastapi_cache.decorator import cache
from fastapi import BackgroundTasks
from tasks.tasks import send_email_up_gymstatus
from fastapi.responses import JSONResponse
from pydantic import ValidationError,EmailStr
from config import ADMIN
from fastapi.responses import RedirectResponse





router = APIRouter(
    tags=["users"],
    prefix="/users"
)


@router.delete("/{id}")
async def delete_one(
    id: int,
    user_service : UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    if user.is_superuser:
        user_id = await user_service.delete_one(id)
        return {"delete_user": user_id}
    raise HTTPException(status_code=403,detail='NOT IS_SUPERUSER')


@router.get('/get_token_to_changepass_by_email')
async def get_token_to_changepass_by_email(
    response: Response,
    email: EmailStr,
    user_service: UserSercvice = Depends(user_service)
):
    res = await user_service.get_token_to_changepass_by_email(email)
    if isinstance(res, HTTPException):
        raise res
    else: 
        response.set_cookie(key="change_pass_cookie", value=res,expires=180)


@router.post("/like_workout/{id}")
async def like_workout(
    id: int,
    user: User = Depends(current_user),
    likedworkout_service: LikedWorkoutService = Depends(likedworkout_service)
):
    res = await likedworkout_service.like_workout(user.id,id)
    if res:
        return {'status':200}
    else:
        raise HTTPException(status_code=404, detail="NOT FOUND WORKOUT")






@router.get("")
@cache(expire=30)
async def find_all(
    user_service:UserSercvice = Depends(user_service),
    user:User = Depends(current_user)
):  
    if user.is_superuser:
        user_all = await user_service.find_all()
        return user_all
    raise HTTPException(status_code=403,detail="Forbidden")
    
@router.get("/filter/direction")

async def find_all_by_direction(
    direction: Direction,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_direction(direction)
    return user_res

@router.get('/verification_user')
async def verification_user(
    response: Response,
    request: Request,
    key: int,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)

):
    token = request.cookies.get('cookie_email_token')
    res = await user_service.verification_user(key,token,user.id)
    response.delete_cookie('cookie_email_token')
    if isinstance(res, dict):
        return res
    else:
        raise res


@router.get('/liked_workout')
async def liked_workout_by_user(
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    res = await user_service.find_liked_workout(user.id)
    return res



@router.get('/changepass_user_by_email')
async def changepass_user_by_email(
    response: Response,
    request: Request,
    key: int,
    new_password: str,
    user_service: UserSercvice = Depends(user_service)
):
    token = request.cookies.get('change_pass_cookie')
    res = await user_service.changepass_by_email_user(key,token,new_password)
    response.delete_cookie('change_pass_cookie')
    if isinstance(res, dict):
        return res
    else:
        raise res
    

@router.get("/filter/gym_status")
@cache(expire=30)
async def find_all_by_fym_status(
    gym_status: GymStatus,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    user_res = await user_service.filter_by_gym_status(gym_status)
    return user_res





@router.get('/verification_get_key')
async def verification_get_key(
    response: Response,
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)  
):
    if not user.is_verified:
        token = await user_service.verification_user_get_token(user.id,user.email)
        response.set_cookie(key="cookie_email_token", value=token,expires=120)
    else:
        raise HTTPException(status_code=409,detail='USER_ALREADY_VERIFIED')

    
@router.get("/get_user_by_email")
async def get_user_info_by_email(
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
):
    if user.is_verified:
        response, tasks= await user_service.get_user_info_by_email(user.id)
        return JSONResponse(response, background=tasks)
    else:
        raise HTTPException(status_code=403,detail="USER IS NOT VERIFIED")


@router.get("/get_current_user")
async def get_user(
    id: int,
    user_service: UserSercvice = Depends(user_service),
    #user: User = Depends(current_user)
):
    user = await user_service.find_one_by_id(id)
    return user


@router.post("/copmpleting_workout")
async def completing_workout(
    user_service: UserSercvice = Depends(user_service),
    user: User = Depends(current_user)
    
):
    response, tasks= await user_service.completing_workout(user.id,user.is_verified)
    if tasks:
        return JSONResponse(response, background=tasks)
    else:
        return response
    













