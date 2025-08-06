from core.domain.repositories.behavior_scale_repository import BehaviorScaleRepository
from rest_framework.exceptions import NotFound

class GetBehaviorScaleService:
    def __init__(self, behavior_scale_repository: BehaviorScaleRepository):
        self.behavior_scale_repository = behavior_scale_repository

    def execute(self, behavior_scale_id: int):
        if not self.behavior_scale_repository.exist_by_id(behavior_scale_id):
            raise NotFound("Behavior scale not found")
        return self.behavior_scale_repository.get(behavior_scale_id)
