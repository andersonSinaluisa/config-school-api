from abc import ABC, abstractmethod
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
    

    
    