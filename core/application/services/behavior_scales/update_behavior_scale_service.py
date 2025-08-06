from core.domain.entities.behavior_scale import BehaviorScale
from core.domain.repositories.behavior_scale_repository import BehaviorScaleRepository
from rest_framework.exceptions import NotFound

class UpdateBehaviorScaleService:
    def __init__(self, behavior_scale_repository: BehaviorScaleRepository):
        self.behavior_scale_repository = behavior_scale_repository

    def execute(self, behavior_scale_id: int, name, minScore, maxScore):
        if not self.behavior_scale_repository.exist_by_id(behavior_scale_id):
            raise NotFound("Behavior scale not found")
        behavior_scale = BehaviorScale(
            id=behavior_scale_id,
            name=name,
            minScore=minScore,
            maxScore=maxScore,
        )
        return self.behavior_scale_repository.update(behavior_scale)
