from core.domain.repositories.section_break_repository import SectionBreakRepository


class ListSectionBreakService:
    def __init__(self, section_break_repository: SectionBreakRepository):
        self.section_break_repository = section_break_repository

    def execute(self, *, section_id=None):
        return self.section_break_repository.all(section_id=section_id)

