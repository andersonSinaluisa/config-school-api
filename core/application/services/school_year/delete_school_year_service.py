

from core.domain.repositories.school_year_repository import SchoolYearRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class DeleteSchoolYearService:
    def __init__(self, school_year_repository:SchoolYearRepository):
        self.school_year_repository = school_year_repository
        
    def execute(self, school_year_id: int):
        """
        Delete a school year by its ID.
        
        Args:
            school_year_id (int): The ID of the school year to delete.
        
        Returns:
            bool: True if the school year was deleted successfully, False otherwise.
        
        Raises:
            NotFound: If the school year with the given ID does not exist.
        """
        try:
            # Delete the school year
            deleted = self.school_year_repository.delete(school_year_id)
            
            return deleted
        except ObjectDoesNotExist:
            raise NotFound(f"School year with ID {school_year_id} does not exist",
                           code="school_year_not_found")