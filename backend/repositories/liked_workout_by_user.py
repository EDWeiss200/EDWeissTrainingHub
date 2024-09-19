from utils.repository import SQLAlchemyRepository

from models.models import LikeWorkoutByUser

class LikedWorkoutRepository(SQLAlchemyRepository):

    model = LikeWorkoutByUser