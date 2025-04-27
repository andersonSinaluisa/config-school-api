from core.domain.entities.level import Level
from core.domain.repositories.level_repository import LevelRepository
from core.models import LevelModel
from django.utils import timezone

class LevelOrmRepository(LevelRepository):
    """Level ORM Adapter for interacting with the LevelModel."""
    def get(self, level_id: int):
        """Get a level by its ID."""
        level = LevelModel.objects.get(id=level_id, deleted=False)
        return Level(
            id=level.id,
            name=level.name,
            description=level.description,
            order=level.order
        )
        
    def all(self):
        """Get all levels."""
        levels = LevelModel.objects.filter(deleted=False)
        return [Level(
            id=level.id,
            name=level.name,
            description=level.description,
            order=level.order
        ) for level in levels]

    def create(self, level: Level):
        """Create a new level."""
        level_model = LevelModel(
            name=level.name,
            description=level.description,
            order=level.order
        )
        level_model.save()
        return Level(
            id=level_model.id,
            name=level_model.name,
            description=level_model.description,
            order=level_model.order
        )

    def update(self, level):
        """Update an existing level."""
        level_model = LevelModel.objects.get(id=level.id, deleted=False)
        level_model.name = level.name
        level_model.description = level.description
        level_model.order = level.order
        level_model.save()
        return Level(
            id=level_model.id,
            name=level_model.name,
            description=level_model.description,
            order=level_model.order
        )
    def delete(self, level_id: str):
        """Delete a level by its ID."""
        level_model = LevelModel.objects.get(id=level_id)
        level_model.deleted = True
        level_model.deleted_at = timezone.now()
        level_model.save()
        return True

    def exist_by_name(self, name: str) -> bool:
        """Check if a level exists by its name."""
        return LevelModel.objects.filter(name=name, deleted=False).exists()

    
    def exist_by_id(self, level_id: int) -> bool:
        """Check if a level exists by its ID."""
        return LevelModel.objects.filter(id=level_id, deleted=False).exists()
