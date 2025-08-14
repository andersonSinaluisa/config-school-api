from abc import ABC, abstractmethod
from typing import List, Dict, Any
from core.domain.entities.school_year import SchoolYear


class SchoolYearRepository(ABC):
    @abstractmethod
    def all(self) -> List[SchoolYear]:
        """Get all school years."""
        pass

    @abstractmethod
    def get(self, school_year_id: int) -> SchoolYear:
        """Get a school year by its ID."""
        pass

    @abstractmethod
    def create(self, school_year: SchoolYear) -> SchoolYear:
        """Create a new school year."""
        pass

    @abstractmethod
    def update(self, school_year: SchoolYear) -> SchoolYear:
        """Update an existing school year."""
        pass

    @abstractmethod
    def delete(self, school_year_id: int) -> None:
        """Delete a school year."""
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> List[SchoolYear]:
        """Find school years by name."""
        pass

    @abstractmethod
    def find_by_date_range(self, start_date: str, end_date: str) -> List[SchoolYear]:
        """Find school years by date range."""
        pass
    
    
    @abstractmethod
    def exist_by_id(self, school_year_id: int) -> bool:
        """Check if a school year exists by its ID."""
        pass
    
    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        """Check if a school year exists by its name."""
        pass

    @abstractmethod
    def find_by_filter(self, **filters) -> List[SchoolYear]:
        """Find school years by the given filter."""
        pass