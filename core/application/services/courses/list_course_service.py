from typing import List

from core.domain.entities.course import Course
from core.domain.repositories.course_repository import CourseRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging


class ListCourseService:
    """Service to list all courses with optional filters."""

    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def execute(self, name: str = None, level_id: int = None) -> List[Course]:
        """Execute the service to list courses with optional filters.

        Args:
            name (str, optional): Filter by course name (partial match).
            level_id (int, optional): Filter by level ID.

        Returns:
            List[Course]: A list of courses matching the filters.
        """
        try:
            filters = {
                "name__icontains": name,
                "level_id": level_id,
            }
            filters = {k: v for k, v in filters.items() if v is not None}
            return self.course_repository.find_by_filter(**filters)
        except Exception as e:
            logging.error(f"Error listing courses: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No courses found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid course data")
            else:
                raise Exception("An unexpected error occurred") from e