from core.domain.repositories.evaluation_type_repository import EvaluationTypeRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListEvaluationTypeService:
    def __init__(self, evaluation_type_repository: EvaluationTypeRepository):
        self.evaluation_type_repository = evaluation_type_repository

    def execute(self):
        try:
            return self.evaluation_type_repository.all()
        except Exception as e:
            logging.error(f"Error listing evaluation types: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No evaluation types found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid evaluation type data")
            else:
                raise Exception("An unexpected error occurred") from e
