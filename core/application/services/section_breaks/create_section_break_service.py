from core.domain.entities.section_break import SectionBreak
from core.domain.repositories.section_break_repository import SectionBreakRepository
from core.domain.repositories.section_repository import SectionRepository
from rest_framework.exceptions import ValidationError


class CreateSectionBreakService:
    def __init__(self, section_break_repository: SectionBreakRepository, section_repository: SectionRepository):
        self.section_break_repository = section_break_repository
        self.section_repository = section_repository

    def execute(self, section_id, day, start_time, end_time):
        if not self.section_repository.exist_by_id(section_id):
            raise ValidationError("Section does not exist", code="invalid_section")

        if self.section_break_repository.exist_by_section_day_time(section_id, day, start_time):
            raise ValidationError("Break already exists at that time", code="duplicate_break")

        section_break = SectionBreak(
            id=None,
            section_id=section_id,
            day=day,
            start_time=start_time,
            end_time=end_time,
        )
        return self.section_break_repository.create(section_break)

