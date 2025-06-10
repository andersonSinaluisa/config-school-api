


from core.domain.repositories.course_subject_repository import CourseSubjectRepository


class RemoveFromCourseService:
    def __init__(self, course_subject_repository: CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, course_id, subject_id):
        # Validate the course subject ID
        if not self.course_subject_repository.exist_by_course_and_subject(course_id, subject_id):
            raise ValueError("Course subject does not exist")

        # Remove the course subject from the course
        self.course_subject_repository.remove_from_course(course_id, subject_id)
        return True