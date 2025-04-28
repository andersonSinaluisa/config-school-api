


from core.domain.repositories.school_year_repository import SchoolYearRepository


class ListSchoolYearService:
    def __init__(self, school_year_repository:SchoolYearRepository):
        self.school_year_repository = school_year_repository

    def execute(self):
        return self.school_year_repository.all()