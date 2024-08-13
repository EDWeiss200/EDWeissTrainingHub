from fastapi_users.authentication import CookieTransport,AuthenticationBackend
from fastapi_users import FastAPIUsers
from .manager import get_user_manager
from .database import User
from fastapi_users.authentication import JWTStrategy
from config import SECRET_AUTH
import fastapi_users
cookie_transport = CookieTransport(cookie_name="gym_cookie",cookie_max_age=7200)



SECRET = SECRET_AUTH

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

