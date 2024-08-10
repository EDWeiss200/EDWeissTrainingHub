from fastapi import FastAPI,Depends
from fastapi_users import FastAPIUsers
from typing import Annotated
from databse import get_async_session,AsyncGenerator
import uvicorn

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.database import User
from auth.schemas import UserCreate,UserRead
app = FastAPI()

#Эндпоинт
@app.get("/")
async def home(db = Depends(get_async_session)):
    return "Hello World"

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

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
uvicorn.run(app)


