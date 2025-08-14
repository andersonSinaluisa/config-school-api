


from core.domain.repositories.school_year_repository import SchoolYearRepository


class ListSchoolYearService:
    def __init__(self, school_year_repository: SchoolYearRepository):
        self.school_year_repository = school_year_repository

    def execute(self, name: str = None, status: str = None):
        filters = {
            "name__icontains": name,
            "status": status,
        }
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.school_year_repository.find_by_filter(**filters)