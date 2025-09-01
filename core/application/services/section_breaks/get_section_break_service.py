from core.domain.repositories.section_break_repository import SectionBreakRepository


class GetSectionBreakService:
    def __init__(self, section_break_repository: SectionBreakRepository):
        self.section_break_repository = section_break_repository

    def execute(self, section_break_id: int):
        return self.section_break_repository.get(section_break_id)

