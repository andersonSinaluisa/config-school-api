from core.domain.repositories.school_year_repository import SchoolYearRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
class GetSchoolYearService:
    def __init__(self, school_year_repository:SchoolYearRepository):
        self.school_year_repository = school_year_repository

    def execute(self, school_year_id: int):
        """
        Get a school year by its ID.
        
        Args:
            school_year_id (int): The ID of the school year to retrieve.
        
        Returns:
            SchoolYear: The school year object if found.
        
        Raises:
            NotFound: If the school year with the given ID does not exist.
        """
        try:
            school_year = self.school_year_repository.get(school_year_id)
            return school_year
        except ObjectDoesNotExist:
            raise NotFound(f"School year with ID {school_year_id} does not exist",
                           code="school_year_not_found")