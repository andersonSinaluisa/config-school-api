from core.domain.entities.behavior_scale import BehaviorScale
from core.domain.repositories.behavior_scale_repository import BehaviorScaleRepository
from core.models import BehaviorScaleModel
from django.utils import timezone

class BehaviorScaleOrmRepository(BehaviorScaleRepository):
    def get(self, behavior_scale_id: int) -> BehaviorScale:
        model = BehaviorScaleModel.objects.get(id=behavior_scale_id, deleted=False)
        return BehaviorScale(
            id=model.id,
            name=model.name,
            minScore=float(model.minScore),
            maxScore=float(model.maxScore),
        )

    def all(self):
        models = BehaviorScaleModel.objects.filter(deleted=False).order_by('name')
        return [
            BehaviorScale(
                id=m.id,
                name=m.name,
                minScore=float(m.minScore),
                maxScore=float(m.maxScore),
            )
            for m in models
        ]

    def create(self, behavior_scale: BehaviorScale) -> BehaviorScale:
        model = BehaviorScaleModel(
            name=behavior_scale.name,
            minScore=behavior_scale.minScore,
            maxScore=behavior_scale.maxScore,
        )
        model.save()
        behavior_scale.id = model.id
        return behavior_scale

    def update(self, behavior_scale: BehaviorScale) -> BehaviorScale:
        model = BehaviorScaleModel.objects.get(id=behavior_scale.id, deleted=False)
        model.name = behavior_scale.name
        model.minScore = behavior_scale.minScore
        model.maxScore = behavior_scale.maxScore
        model.save()
        return behavior_scale

    def delete(self, behavior_scale_id: int) -> bool:
        model = BehaviorScaleModel.objects.get(id=behavior_scale_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_name(self, name: str) -> bool:
        return BehaviorScaleModel.objects.filter(name=name, deleted=False).exists()

    def exist_by_id(self, behavior_scale_id: int) -> bool:
        return BehaviorScaleModel.objects.filter(id=behavior_scale_id, deleted=False).exists()
