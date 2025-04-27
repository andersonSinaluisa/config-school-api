# -*- coding: utf-8 -*-
from core.domain.repositories.course_repository import CourseRepository
from rest_framework.exceptions import NotFound, ValidationError

class DeleteCourseService:
    def __init__(self, course_repository:CourseRepository):
        self.course_repository = course_repository
  

    def execute(self, course_id: int):
        # Check if the course exists
        print('course_id', course_id)
        course = self.course_repository.get(course_id)
        if not course:
            raise NotFound(f"Course with ID {course_id} does not exist",
                           code="course_not_found")

        # Delete the course
        self.course_repository.delete(course_id)
        return course