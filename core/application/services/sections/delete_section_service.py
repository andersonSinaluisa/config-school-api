
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError, ErrorDetail

from core.domain.repositories.section_repository import SectionRepository
class DeleteSectionService:
    def __init__(self, section_repository:SectionRepository):
        self.section_repository = section_repository

    def execute(self, section_id):
        # Validate the section ID
        try:
            self.section_repository.delete(section_id)
        except ObjectDoesNotExist:
            raise ValidationError("Section not found.", code=ErrorDetail(string="id", code="not_found"))
        except Exception as e:
            raise ValidationError(f"An error occurred while deleting the section: {str(e)}", code=ErrorDetail(string="id", code="error"))