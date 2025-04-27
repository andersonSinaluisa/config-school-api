
from django.core.exceptions import ObjectDoesNotExist
from core.domain.repositories.level_repository import LevelRepository
from rest_framework.exceptions import NotFound

class GetLevelService:
    def __init__(self, level_repository:LevelRepository):
        self.level_repository = level_repository

    def execute(self, level_id):
        """
        Retrieves a level by its ID.

        :param level_id: The ID of the level to retrieve.
        :return: The level object if found, None otherwise.
        """
        try:
            return self.level_repository.get(level_id)
        except ObjectDoesNotExist:
            raise NotFound("Level not found")