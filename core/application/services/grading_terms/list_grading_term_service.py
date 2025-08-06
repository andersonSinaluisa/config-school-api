from core.domain.repositories.grading_term_repository import GradingTermRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListGradingTermService:
    def __init__(self, grading_term_repository: GradingTermRepository):
        self.grading_term_repository = grading_term_repository

    def execute(self):
        try:
            return self.grading_term_repository.all()
        except Exception as e:
            logging.error(f"Error listing grading terms: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No grading terms found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid grading term data")
            else:
                raise Exception("An unexpected error occurred") from e
