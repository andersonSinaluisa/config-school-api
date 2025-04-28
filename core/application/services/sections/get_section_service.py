

from core.domain.repositories.section_repository import SectionRepository
from rest_framework.exceptions import ValidationError, ErrorDetail
from django.core.exceptions import ObjectDoesNotExist

class GetSectionService:
    def __init__(self, section_repository:SectionRepository):
        self.section_repository = section_repository

    def execute(self, section_id):
        """
        Retrieves a section by its ID.

        :param section_id: The ID of the section to retrieve.
        :return: The section object if found, None otherwise.
        """
        try:
            return self.section_repository.get(section_id)
        except ObjectDoesNotExist:
            raise ValidationError("Section not found.", code=ErrorDetail(string="id", code="not_found"))
        except Exception as e:
            raise ValidationError(f"An error occurred while retrieving the section: {str(e)}", code=ErrorDetail(string="id", code="error"))