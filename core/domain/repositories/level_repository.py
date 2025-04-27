from abc import ABC, abstractmethod
class LevelRepository(ABC):
    @abstractmethod
    def get(self, level_id: int):
        """Get a level by its ID."""
        pass

    @abstractmethod
    def all(self):
        """Get all levels."""
        pass

    @abstractmethod
    def create(self, level):
        """Create a new level."""
        pass

    @abstractmethod
    def update(self, level):
        """Update an existing level."""
        pass

    @abstractmethod
    def delete(self, level_id: str):
        """Delete a level by its ID."""
        pass

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        """Check if a level exists by its name."""
        pass
    
    @abstractmethod
    def exist_by_id(self, level_id: int) -> bool:
        """Check if a level exists by its ID."""
        pass