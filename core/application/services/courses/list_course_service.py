from typing import List
from core.domain.entities.course import Course
from core.domain.repositories.course_repository import CourseRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging
class ListCourseService:
    """Service to list all courses."""
    def __init__(self, course_repository:CourseRepository):
        self.course_repository = course_repository

    def execute(self) -> List[Course]:
        """Execute the service to list all courses.
        Returns:
            list: A list of all courses.
        """
        try:
            return self.course_repository.all()
        except Exception as e:
            logging.error(f"Error listing courses: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No courses found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid course data")
            else:
                raise Exception("An unexpected error occurred") from e