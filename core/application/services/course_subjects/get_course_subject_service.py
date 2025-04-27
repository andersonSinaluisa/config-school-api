

from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, server_error

class GetCourseSubjectService:
    def __init__(self, course_subject_repository:CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, course_subject_id):
        try:
            return self.course_subject_repository.get(course_subject_id)
        except ObjectDoesNotExist as e:
            raise NotFound("Course subject not found") from e