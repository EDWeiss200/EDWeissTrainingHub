from abc import ABC,abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload,load_only,joinedload
from models.models import User

class AbstractRelationShipStrategy(ABC):

    @abstractmethod
    async def selectinload_query():
        raise NotImplementedError

    @abstractmethod
    async def joinedloadSRS():
        raise NotImplementedError


class UserRelationshipStrategy(AbstractRelationShipStrategy):

    async def selectinload_query(stmt,loadOnly,user_id):
        query = (
            select(User)
            .where(User.id == user_id)
            .options(selectinload(stmt))
            
        )
        return query

            