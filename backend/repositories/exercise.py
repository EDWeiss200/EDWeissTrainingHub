from utils.repository import SQLAlchemyRepository
from models.models import Exercise

class ExerciseRepository(SQLAlchemyRepository):

    model = Exercise