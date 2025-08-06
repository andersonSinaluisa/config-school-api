from core.domain.entities.behavior_scale import BehaviorScale
from core.domain.repositories.behavior_scale_repository import BehaviorScaleRepository
from rest_framework.exceptions import ValidationError

class CreateBehaviorScaleService:
    def __init__(self, behavior_scale_repository: BehaviorScaleRepository):
        self.behavior_scale_repository = behavior_scale_repository

    def execute(self, name, minScore, maxScore):
        if self.behavior_scale_repository.exist_by_name(name):
            raise ValidationError("Behavior scale with this name already exists.")
        behavior_scale = BehaviorScale(
            id=None,
            name=name,
            minScore=minScore,
            maxScore=maxScore,
        )
        return self.behavior_scale_repository.create(behavior_scale)
