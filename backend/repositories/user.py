from utils.repository import SQLAlchemyRepository
from utils.strategy import UserRelationshipStrategy
from models.models import User

class UserRepository(SQLAlchemyRepository):

    model = User
    strategy = UserRelationshipStrategy