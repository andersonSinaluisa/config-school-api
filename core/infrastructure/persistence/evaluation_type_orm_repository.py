from core.domain.entities.evaluation_type import EvaluationType
from core.domain.repositories.evaluation_type_repository import EvaluationTypeRepository
from core.models import EvaluationTypeModel
from django.utils import timezone

class EvaluationTypeOrmRepository(EvaluationTypeRepository):
    def get(self, evaluation_type_id: int) -> EvaluationType:
        model = EvaluationTypeModel.objects.get(id=evaluation_type_id, deleted=False)
        return EvaluationType(
            id=model.id,
            name=model.name,
            description=model.description,
            weight=float(model.weight),
        )

    def all(self):
        models = EvaluationTypeModel.objects.filter(deleted=False).order_by('name')
        return [
            EvaluationType(
                id=m.id,
                name=m.name,
                description=m.description,
                weight=float(m.weight),
            )
            for m in models
        ]

    def create(self, evaluation_type: EvaluationType) -> EvaluationType:
        model = EvaluationTypeModel(
            name=evaluation_type.name,
            description=evaluation_type.description,
            weight=evaluation_type.weight,
        )
        model.save()
        evaluation_type.id = model.id
        return evaluation_type

    def update(self, evaluation_type: EvaluationType) -> EvaluationType:
        model = EvaluationTypeModel.objects.get(id=evaluation_type.id, deleted=False)
        model.name = evaluation_type.name
        model.description = evaluation_type.description
        model.weight = evaluation_type.weight
        model.save()
        return evaluation_type

    def delete(self, evaluation_type_id: int) -> bool:
        model = EvaluationTypeModel.objects.get(id=evaluation_type_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_name(self, name: str) -> bool:
        return EvaluationTypeModel.objects.filter(name=name, deleted=False).exists()

    def exist_by_id(self, evaluation_type_id: int) -> bool:
        return EvaluationTypeModel.objects.filter(id=evaluation_type_id, deleted=False).exists()
