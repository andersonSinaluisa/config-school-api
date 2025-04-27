


from core.domain.repositories.subject_repository import SubjectRepository
from rest_framework.exceptions import NotFound, ValidationError
from django.core.exceptions import ObjectDoesNotExist

class DeleteSubjectService:
    def __init__(self, subject_repository:SubjectRepository):
        self.subject_repository = subject_repository

    def execute(self, subject_id):
        try:
        # Delete the subject
            self.subject_repository.delete(subject_id)
            return True
        except ObjectDoesNotExist:
            raise NotFound("Subject not found")