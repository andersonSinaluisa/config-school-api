from core.domain.entities.subject import Subject
from core.domain.repositories.subject_repository import SubjectRepository
import logging
from rest_framework.exceptions import ValidationError, NotFound
class CreateSubjectService:
    def __init__(self, subject_repository:SubjectRepository):
        self.subject_repository = subject_repository
        
    def execute(self, name, description, code, hoursPerWeek):
        """
        Create a new subject.
        Args:
            subject_data (dict): A dictionary containing subject data.
        Returns:
            dict: The created subject object.
        """
        new_subject = Subject(
            id=None,
            name=name,
            description=description,
            code=code,
            hoursPerWeek=hoursPerWeek
        )
        if self.subject_repository.exist_by_name(name):
            raise ValidationError("Subject with this name already exists")
        return self.subject_repository.create(new_subject)
        

    