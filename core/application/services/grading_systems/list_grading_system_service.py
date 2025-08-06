from core.domain.repositories.grading_system_repository import GradingSystemRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListGradingSystemService:
    def __init__(self, grading_system_repository: GradingSystemRepository):
        self.grading_system_repository = grading_system_repository

    def execute(self):
        try:
            return self.grading_system_repository.all()
        except Exception as e:
            logging.error(f"Error listing grading systems: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No grading systems found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid grading system data")
            else:
                raise Exception("An unexpected error occurred") from e
