from core.domain.repositories.behavior_scale_repository import BehaviorScaleRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListBehaviorScaleService:
    def __init__(self, behavior_scale_repository: BehaviorScaleRepository):
        self.behavior_scale_repository = behavior_scale_repository

    def execute(self):
        try:
            return self.behavior_scale_repository.all()
        except Exception as e:
            logging.error(f"Error listing behavior scales: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No behavior scales found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid behavior scale data")
            else:
                raise Exception("An unexpected error occurred") from e
