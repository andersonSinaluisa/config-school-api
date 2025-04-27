

from core.domain.entities.subject import Subject
from core.domain.repositories.subject_repository import SubjectRepository
from rest_framework.exceptions import NotFound, ValidationError

class UpdateSubjectService:
    def __init__(self, subject_repository:SubjectRepository):
        """Initialize the service with a subject repository.
        Args:
            subject_repository (SubjectRepository): The repository to interact with subject data.
        """
        self.subject_repository = subject_repository
    def execute(self, name, code, description, hoursPerWeek, id):
        """
        Update an existing subject.
        Args:
            subject_data (dict): A dictionary containing subject data.
        Returns:
            Subject: The updated subject object.
        """
        updated_subject = Subject(
            id=id,
            name=name,
            code=code,
            description=description,
            hoursPerWeek=hoursPerWeek
        )
        if self.subject_repository.exist_by_name(name):
            raise ValidationError(f"Subject with name {name} already exists",
                                  code="subject_name_exists")
        if not self.subject_repository.exist_by_id(id):
            raise NotFound(f"Subject with ID {id} does not exist",
                           code="subject_not_found")
        
        return self.subject_repository.update(updated_subject)