from core.domain.entities.section import Section
from core.domain.repositories.section_repository import SectionRepository
from rest_framework.exceptions import ValidationError, ErrorDetail
from django.core.exceptions import ObjectDoesNotExist

class UpdateSectionService:
    def __init__(self, section_repository:SectionRepository):
        self.section_repository = section_repository

    def execute(self, id: int, name: str, type: str, description: str, ):
        # Validate the section data
        try:
            
            section = Section(
                id=id,
                name=name,
                type=type,
                description=description
            )
            
            # Update the section in the repository
            updated_section = self.section_repository.update(section)
            return updated_section
        
        except ObjectDoesNotExist:
            raise ValidationError("Section not found.", code=ErrorDetail(string="id", code="not_found"))
        except Exception as e:
            raise ValidationError(f"An error occurred while updating the section: {str(e)}", code=ErrorDetail(string="id", code="error"))