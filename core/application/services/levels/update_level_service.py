

from core.domain.entities.level import Level
from core.domain.repositories.level_repository import LevelRepository
from rest_framework.exceptions import ValidationError, NotFound

class UpdateLevelService:
    def __init__(self, level_repository:LevelRepository):
        self.level_repository = level_repository

    def execute(self, id, name,description, order):
        # Validate the updated data
        level = self.level_repository.exist_by_id(id)
        if not level:
            raise NotFound(f"Level with ID {id} not found")
        
        if self.level_repository.exist_by_name(name):
            raise ValidationError(f"Level with name {name} already exists")
        
        updated_level = Level(
            id=id,
            name=name,
            description=description,
            order=order
        )

        # Update the level in the repository
        updated_level = self.level_repository.update(updated_level)
        return updated_level