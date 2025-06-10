from core.domain.repositories.course_subject_repository import CourseSubjectRepository


class ListCourseSubjectService:
    def __init__(self, course_subject_repository:CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self):
        return self.course_subject_repository.all()

