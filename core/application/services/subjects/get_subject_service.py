

from core.domain.repositories.subject_repository import SubjectRepository
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

class GetSubjectService:
    def __init__(self, subject_repository: SubjectRepository):
        """Initialize the service with a subject repository.
        Args:
            subject_repository (SubjectRepository): The repository to interact with subject data.
        """
        self.subject_repository = subject_repository
        
        
    def execute(self, subject_id):
        """
        Retrieves a subject by its ID.
        Args:
            subject_id (int): The ID of the subject to retrieve.
        Returns:
            Subject: The subject object if found.
        Raises:
            NotFound: If the subject with the given ID does not exist.
        """
        try:
            return self.subject_repository.get(subject_id)
        except ObjectDoesNotExist:
            raise NotFound("Subject not found")