from core.domain.entities.section_break import SectionBreak
from core.domain.repositories.section_break_repository import SectionBreakRepository
from core.domain.repositories.section_repository import SectionRepository
from rest_framework.exceptions import ValidationError


class UpdateSectionBreakService:
    def __init__(self, section_break_repository: SectionBreakRepository, section_repository: SectionRepository):
        self.section_break_repository = section_break_repository
        self.section_repository = section_repository

    def execute(self, section_break_id: int, section_id, day, start_time, end_time):
        if not self.section_break_repository.exist_by_id(section_break_id):
            raise ValidationError("Section break does not exist", code="invalid_section_break")

        if not self.section_repository.exist_by_id(section_id):
            raise ValidationError("Section does not exist", code="invalid_section")

        section_break = SectionBreak(
            id=section_break_id,
            section_id=section_id,
            day=day,
            start_time=start_time,
            end_time=end_time,
        )
        return self.section_break_repository.update(section_break)

