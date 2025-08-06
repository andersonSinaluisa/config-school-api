from core.domain.entities.grading_term import GradingTerm
from core.domain.repositories.grading_term_repository import GradingTermRepository
from core.models import GradingTermModel
from django.utils import timezone

class GradingTermOrmRepository(GradingTermRepository):
    def get(self, grading_term_id: int) -> GradingTerm:
        model = GradingTermModel.objects.get(id=grading_term_id, deleted=False)
        return GradingTerm(
            id=model.id,
            gradingSystem_id=model.gradingSystem_id,
            academicYear_id=model.academicYear_id,
            name=model.name,
            order=model.order,
            weight=float(model.weight),
        )

    def all(self):
        models = GradingTermModel.objects.filter(deleted=False).order_by('order')
        return [
            GradingTerm(
                id=m.id,
                gradingSystem_id=m.gradingSystem_id,
                academicYear_id=m.academicYear_id,
                name=m.name,
                order=m.order,
                weight=float(m.weight),
            )
            for m in models
        ]

    def create(self, grading_term: GradingTerm) -> GradingTerm:
        model = GradingTermModel(
            gradingSystem_id=grading_term.gradingSystem_id,
            academicYear_id=grading_term.academicYear_id,
            name=grading_term.name,
            order=grading_term.order,
            weight=grading_term.weight,
        )
        model.save()
        grading_term.id = model.id
        return grading_term

    def update(self, grading_term: GradingTerm) -> GradingTerm:
        model = GradingTermModel.objects.get(id=grading_term.id, deleted=False)
        model.gradingSystem_id = grading_term.gradingSystem_id
        model.academicYear_id = grading_term.academicYear_id
        model.name = grading_term.name
        model.order = grading_term.order
        model.weight = grading_term.weight
        model.save()
        return grading_term

    def delete(self, grading_term_id: int) -> bool:
        model = GradingTermModel.objects.get(id=grading_term_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_id(self, grading_term_id: int) -> bool:
        return GradingTermModel.objects.filter(id=grading_term_id, deleted=False).exists()
