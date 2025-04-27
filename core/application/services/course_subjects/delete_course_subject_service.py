


from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError

class DeleteCourseSubjectService:
    def __init__(self, course_subject_repository:CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, id:int):
        """
        Delete an existing course subject.
        Args:
            id (int): The ID of the course subject to delete.
        Returns:
            bool: True if the course subject was deleted successfully, False otherwise.
        """
        try:
            return self.course_subject_repository.delete(id)
        except ObjectDoesNotExist:
            raise NotFound(f"CourseSubject with ID {id} does not exist",
                           code="course_subject_not_found")
            