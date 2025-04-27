from core.domain.repositories.course_repository import CourseRepository
from rest_framework.exceptions import NotFound, ValidationError
from django.core.exceptions import ObjectDoesNotExist
class GetCourseService:

    def __init__(self, course_repository:CourseRepository):
        self.course_repository = course_repository

    def execute(self, course_id):
        try:
            return self.course_repository.get(course_id)
       
        except ObjectDoesNotExist:
            raise NotFound("Course not found")
            