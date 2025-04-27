

from core.domain.repositories.level_repository import LevelRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging
class ListLevelService:
    def __init__(self, level_repository:LevelRepository):
        self.level_repository = level_repository

    def execute(self):
        try:
            return self.level_repository.all()
        except Exception as e:
            logging.error(f"Error listing levels: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No levels found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid level data")
            else:
                raise Exception("An unexpected error occurred") from e