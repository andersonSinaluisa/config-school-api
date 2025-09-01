from core.domain.repositories.section_break_repository import SectionBreakRepository
from rest_framework.exceptions import ValidationError


class DeleteSectionBreakService:
    def __init__(self, section_break_repository: SectionBreakRepository):
        self.section_break_repository = section_break_repository

    def execute(self, section_break_id: int):
        if not self.section_break_repository.exist_by_id(section_break_id):
            raise ValidationError("Section break does not exist", code="invalid_section_break")
        return self.section_break_repository.delete(section_break_id)

