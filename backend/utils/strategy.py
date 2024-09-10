from abc import ABC,abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload,load_only,joinedload
from models.models import User

class AbstractRelationShipStrategy(ABC):

    @abstractmethod
    async def liked_workout_by_user():
        raise NotImplementedError



class UserRelationshipStrategy(AbstractRelationShipStrategy):

    async def liked_workout_by_user(stmt,loadOnly,user_id):
        query = (
            select(User)
            .where(User.id == user_id)
            .options(selectinload(stmt))
            
        )
        return query

            