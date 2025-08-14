from abc import ABC, abstractmethod
from typing import List

from core.domain.entities.course import Course
class CourseRepository(ABC):
    
    @abstractmethod
    def get(self, course_id: str):
        """Get a course by its ID."""
        pass
    
    @abstractmethod
    def all(self):
        """Get all courses."""
        pass
    
    @abstractmethod
    def create(self, course: Course) -> Course:
        """Create a new course."""
        pass
    
    @abstractmethod
    def update(self, course:    Course):
        """Update an existing course."""
        pass
    
    @abstractmethod
    def delete(self, course_id: str):
        """Delete a course by its ID."""
        pass
    

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        """Check if a course exists by its name."""
        pass
    
    @abstractmethod
    def exist_by_id(self, course_id: str) -> bool:
        """Check if a course exists by its ID."""
        pass

    @abstractmethod
    def find_by_filter(self, **filters) -> List[Course]:
        """Find courses by the given filter."""
        pass
    