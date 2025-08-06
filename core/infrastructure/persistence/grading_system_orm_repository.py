from core.domain.entities.grading_system import GradingSystem
from core.domain.repositories.grading_system_repository import GradingSystemRepository
from core.models import GradingSystemModel
from django.utils import timezone

class GradingSystemOrmRepository(GradingSystemRepository):
    def get(self, grading_system_id: int) -> GradingSystem:
        model = GradingSystemModel.objects.get(id=grading_system_id, deleted=False)
        return GradingSystem(
            id=model.id,
            name=model.name,
            description=model.description,
            numberOfTerms=model.numberOfTerms,
            passingScore=float(model.passingScore),
        )

    def all(self):
        models = GradingSystemModel.objects.filter(deleted=False).order_by('name')
        return [
            GradingSystem(
                id=m.id,
                name=m.name,
                description=m.description,
                numberOfTerms=m.numberOfTerms,
                passingScore=float(m.passingScore),
            )
            for m in models
        ]

    def create(self, grading_system: GradingSystem) -> GradingSystem:
        model = GradingSystemModel(
            name=grading_system.name,
            description=grading_system.description,
            numberOfTerms=grading_system.numberOfTerms,
            passingScore=grading_system.passingScore,
        )
        model.save()
        grading_system.id = model.id
        return grading_system

    def update(self, grading_system: GradingSystem) -> GradingSystem:
        model = GradingSystemModel.objects.get(id=grading_system.id, deleted=False)
        model.name = grading_system.name
        model.description = grading_system.description
        model.numberOfTerms = grading_system.numberOfTerms
        model.passingScore = grading_system.passingScore
        model.save()
        return grading_system

    def delete(self, grading_system_id: int) -> bool:
        model = GradingSystemModel.objects.get(id=grading_system_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_name(self, name: str) -> bool:
        return GradingSystemModel.objects.filter(name=name, deleted=False).exists()

    def exist_by_id(self, grading_system_id: int) -> bool:
        return GradingSystemModel.objects.filter(id=grading_system_id, deleted=False).exists()
