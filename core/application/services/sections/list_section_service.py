


from core.domain.repositories.section_repository import SectionRepository


class ListSectionService:
    def __init__(self, section_repository:SectionRepository):
        self.section_repository = section_repository

    def execute(self):
        return self.section_repository.all()