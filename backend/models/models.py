from sqlalchemy import MetaData,String,Integer,Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Boolean, ForeignKey, Integer, String, func, select,Column
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

metadata = MetaData()

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer,index = True, primary_key=True)
    name = Column(String)


class User(Base):
    __tablename__= "users"
    id = Column(Integer,index =True,primary_key = True)
    username = Column(String,nullable=False)
    email = Column(String,nullable=False)
    gender = Column(String,nullable=False)
    weight = Column(Integer,nullable=False)
    height = Column(Integer,nullable=False)
    direction = Column(String,nullable=False)
    gym_status = Column(String,nullable=False)
    days_of_training = Column(Integer)
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    