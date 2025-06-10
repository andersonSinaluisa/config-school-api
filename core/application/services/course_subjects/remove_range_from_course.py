
from typing import List
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from core.domain.entities.couse_subject import CourseSubject


class RemoveRangeFromCourse:
    """
    Service to remove a range of subjects from a course.
    """

    def __init__(self, course_subject_repository: CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, course_subjects: List[int]):
        # Logic to remove the subjects from the course
        if not course_subjects:
            raise ValueError("Course subjects list cannot be empty")
        
        
        
        self.course_subject_repository.remove_range_from_course(course_subjects)