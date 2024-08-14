from abc import ABC,abstractmethod
from databse import async_session_maker
from sqlalchemy import insert,select,delete,update


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one():
        raise NotImplementedError
    
    @abstractmethod
    async def filter():
        raise NotImplementedError
    
    @abstractmethod
    async def update():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):

    model = None

    async def add_one(self, data : dict) -> int:
        async with async_session_maker() as session:
            stmt = (
                insert(self.model).
                values(**data).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
      async with async_session_maker() as session:
            stmt = (
                select(self.model)
            )
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    
    async def delete_one(self,id):
        async with async_session_maker() as session:
            stmt = (
                delete(self.model).
                where(self.model.id == id)
            )
            await session.execute(stmt)
            await session.commit()
            return id

    async def filter(self,filters: list):
        async with async_session_maker() as session:
            stmt =(
                select(self.model).filter(*filters)
            )
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
        
    async def update(self,id,values: dict):
        async with async_session_maker() as session:
            stmt = (
                update(self.model).
                where(self.model.id == id).
                values(**values).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()


