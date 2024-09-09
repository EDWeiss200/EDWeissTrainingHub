
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, ForeignKey, Integer, String, func, select,Column,MetaData

from schemas.schemas import UserInfo,ExerciseSchema,WorkoutSchema
metadata = MetaData()

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__= "users"
    id = Column(Integer,index =True,primary_key = True)
    username = Column(String,nullable=False)
    email = Column(String,nullable=False)
    gender = Column(String,nullable=False)
    weight = Column(Integer,nullable=False)
    height = Column(Integer,nullable=False)
    direction = Column(String,nullable=False)
    gym_status = Column(String,nullable=False)
    count_workout = Column(Integer,nullable=False)
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

    workout_liked: Mapped[list['Workout']] = relationship(
        back_populates='user_liked',
        secondary="likes_workout_by_user"
    )

    def to_read_model(self) -> UserInfo:
        return UserInfo(
            id = self.id,
            username = self.username,
            email = self.email,
            gender = self.gender,
            weight=self.weight,
            height=self.height,
            direction=self.direction,
            gym_status=self.gym_status,
            count_workout = self.count_workout,
        ) 



class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer,index = True,primary_key = True)
    author_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    name = Column(String,nullable=False)
    muscle_group = Column(String,nullable=False)
    number_of_repetitions = Column(Integer,nullable=False)
    number_of_approaches = Column(Integer,nullable=False)
    break_between_approaches = Column(Integer,nullable=False)
    workload = Column(Integer,nullable=False)

    def to_read_model(self) -> ExerciseSchema:
        return ExerciseSchema(
            id = self.id,
            author_id = self.author_id,
            name = self.name,
            muscle_group = self.muscle_group,
            number_of_repetitions = self.number_of_repetitions,
            number_of_approaches=self.number_of_approaches,
            break_between_approaches = self.break_between_approaches,
            workload = self.workload
        ) 


class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer,index = True,primary_key = True)
    author_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    break_between_exercises = Column(Integer,nullable=False)
    direction = Column(String,nullable=False)
    exercise_1id = Column(Integer,ForeignKey("exercises.id"), nullable=False)
    exercise_2id = Column(Integer,ForeignKey("exercises.id"), nullable=True)
    exercise_3id = Column(Integer,ForeignKey("exercises.id"), nullable=True)
    exercise_4id = Column(Integer,ForeignKey("exercises.id"), nullable=True)
    exercise_5id = Column(Integer,ForeignKey("exercises.id"), nullable=True)
    
    user_liked: Mapped[list["User"]] = relationship(
        back_populates='workout_liked',
        secondary="likes_workout_by_user"
    )

    def to_read_model(self) -> WorkoutSchema:
        return WorkoutSchema(
            id=self.id,
            author_id=self.author_id,
            name = self.name,
            break_between_exercises=self.break_between_exercises,
            direction=self.direction,
            exercise_1id=self.exercise_1id,
            exercise_2id=self.exercise_2id,
            exercise_3id=self.exercise_3id,
            exercise_4id=self.exercise_4id,
            exercise_5id=self.exercise_5id,
            like_count=self.like_count
        )
    


class LikeWorkoutByUser(Base):
    __tablename__ = "likes_workout_by_user"

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id',ondelete='CASCADE'),
        primary_key=True
    )
    workout_id: Mapped[int] = mapped_column(
        ForeignKey('workout.id',ondelete='CASCADE'),
        primary_key=True
    )
    