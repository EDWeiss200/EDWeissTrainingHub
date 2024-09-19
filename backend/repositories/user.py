from utils.repository import SQLAlchemyRepository

from models.models import User

class UserRepository(SQLAlchemyRepository):

    model = User
