from fastapi import FastAPI,Depends
from fastapi_users import FastAPIUsers
from typing import Annotated
from databse import get_async_session,AsyncGenerator
import uvicorn
from auth.auth import auth_backend,fastapi_users
from auth.schemas import UserCreate,UserRead
from api.exercise_router import router as exercise_router
from api.user_router import router as user_router
from api.workout_router import router as workout_router


app = FastAPI()

#Эндпоинт
@app.get("/")
async def home(db = Depends(get_async_session)):
    return "Hello World"


#авторизация
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(user_router)
app.include_router(workout_router)
app.include_router(exercise_router)

uvicorn.run(app)






