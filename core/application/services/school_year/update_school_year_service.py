


from core.domain.entities.school_year import SchoolYear
from core.domain.repositories.school_year_repository import SchoolYearRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
class UpdateSchoolYearService:
    def __init__(self, school_year_repository:SchoolYearRepository):
        self.school_year_repository = school_year_repository
        
    def execute(self, school_year_id: int, name: str, startDate: str, endDate: str, status: str):
        """
        Update a school year by its ID.
        
        Args:
            school_year_id (int): The ID of the school year to update.
            name (str): The new name of the school year.
            startDate (str): The new start date of the school year.
            endDate (str): The new end date of the school year.
            status (str): The new status of the school year.
        
        Returns:
            SchoolYear: The updated school year object.
        
        Raises:
            NotFound: If the school year with the given ID does not exist.
        """
        try:
            # Update the school 
            school_year = SchoolYear(
                id=school_year_id,
                name=name,
                startDate=startDate,
                endDate=endDate,
                status=status
            )
            updated_school_year = self.school_year_repository.update(
                school_year)
            
            return updated_school_year
        except ObjectDoesNotExist:
            raise NotFound(f"School year with ID {school_year_id} does not exist",
                           code="school_year_not_found")