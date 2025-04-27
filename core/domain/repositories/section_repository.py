from abc import ABC, abstractmethod
from typing import List

from core.domain.entities.section import Section 

class SectionRepository(ABC):
    @abstractmethod
    def all(self) -> List[Section]:
        """Get all sections."""
        pass
    
    @abstractmethod
    def get(self, section_id: int) -> Section:
        """Get a section by its ID."""
        pass
    
    
    @abstractmethod
    def create(self, section: Section) -> Section:
        """Create a new section."""
        pass
    
    
    @abstractmethod
    def update(self, section: Section) -> Section:
        """Update an existing section."""
        pass
    
    
    @abstractmethod
    def delete(self, section_id: int) -> None:
        """Delete a section by its ID."""
        pass
    
    
    @abstractmethod
    def exist_by_id(self, section_id: int) -> bool:
        """Check if a section exists by its ID."""
        pass
    
    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        """Check if a section exists by its name."""
        pass
    
    
    