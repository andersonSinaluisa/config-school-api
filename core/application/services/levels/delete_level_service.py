

from core.domain.repositories.level_repository import LevelRepository
import logging
from rest_framework.exceptions import NotFound, ValidationError
class DeleteLevelService:
    def __init__(self, level_repository:LevelRepository):
        self.level_repository = level_repository

    def execute(self, level_id):
        # Check if the level exists
        level = self.level_repository.exist_by_id(level_id)
        if not level:
            logging.error(f"Level with ID {level_id} not found.")
            raise NotFound(f"Level with ID {level_id} not found.")

        # Delete the level
        self.level_repository.delete_level(level_id)
        return True  # Return a success message or status if needed