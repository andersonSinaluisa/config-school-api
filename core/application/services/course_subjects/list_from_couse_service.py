
from core.domain.repositories.course_subject_repository import CourseSubjectRepository

class ListFromCourseService:
    def __init__(self, course_subject_repository: CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, course_id):
        return self.course_subject_repository.get_by_course(course_id)
