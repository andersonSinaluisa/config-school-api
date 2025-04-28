from core.domain.entities.couse_subject import CourseSubject
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
class UpdateCourseSubjectService:
    def __init__(self, course_subject_repository:CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, id:int, courseId:int, subjectId:int, hoursPerWeek:int, isRequired:bool):
        """
        Update an existing course subject.
        Args:
            id (int): The ID of the course subject to update.
            course_id (int): The ID of the course.
            subject_id (int): The ID of the subject.
            hours_per_week (int): The number of hours per week.
            is_required (bool): Whether the subject is required or not.
        Returns:
            CourseSubject: The updated course subject object.
        """
        try:
            course_subject = CourseSubject(
                id=id,
                courseId=courseId,
                subjectId=subjectId,
                hoursPerWeek=hoursPerWeek,
                isRequired=isRequired
            )
            
            return self.course_subject_repository.update(course_subject)
        except ObjectDoesNotExist:
            raise NotFound(f"CourseSubject with ID {id} does not exist",
                           code="course_subject_not_found")