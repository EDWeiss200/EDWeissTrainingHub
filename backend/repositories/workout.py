from utils.repository import SQLAlchemyRepository
from models.models import Workout

class WorkoutRepository(SQLAlchemyRepository):

    model = Workout