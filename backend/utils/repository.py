from abc import ABC,abstractmethod
from databse import async_session_maker
from sqlalchemy import insert,select,delete,update,func,column,join,desc
from sqlalchemy.orm import selectinload,load_only
from models.models import Workout

class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def add_one_not_return():
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

    @abstractmethod
    async def relationship_base_find():
        raise NotImplementedError

    @abstractmethod
    async def find_count():
        raise NotImplementedError

    @abstractmethod
    async def find_and_sort():
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
    
    async def add_one_not_return(self, data : dict) -> int:
        async with async_session_maker() as session:
            stmt = (
                insert(self.model).
                values(**data)
            )
            await session.execute(stmt)
            await session.commit()
            return True

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
    
    async def update_by_filter(self,filter,values: dict):
        async with async_session_maker() as session:
            stmt = (
                update(self.model).
                where(*filter).
                values(**values).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def relationship_base_find(self,relationship,column):
        async with async_session_maker() as session:  
            #query = await self.strategy.relationship_query(relationship,user_id)
            #query = await RelationShipQuery.relationship_query(self.model,relationship,user_id)
            query = (
                select(self.model)
                .where(self.model.id == column)
                .options(selectinload(relationship))
                
            )
            res =  await session.execute(query)
            result_orm = res.scalars().all()

            return result_orm


    async def find_count(self,group,lim):
        async with async_session_maker() as session:  
            query = (
                select(
                    column(group),
                    func.count()
                )
                .select_from(self.model)
                .group_by(group)
            )

            res = await session.execute(query)
            return res.all()

    async def find_and_sort(self,collumn,lim = 5,sort_filter = False):
        async with async_session_maker() as session:  
            query = select(self.model)
            if not sort_filter:
                query = (query.order_by(collumn).limit(lim))
            if sort_filter:
                query = (query.order_by(desc(collumn)).limit(lim))
            res = await session.execute(query)
            return res.scalars().all()

    async def find_row_number_in_sort(self,column):
        async with async_session_maker() as session:  
            query = (
                select(
                    func.row_number().over(
                        order_by=desc(column)
                    ),
                    self.model.id
                )   
            )
            res = await session.execute(query)
            return res.all()



