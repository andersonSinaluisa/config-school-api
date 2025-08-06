from core.domain.entities.grading_term import GradingTerm
from core.domain.repositories.grading_term_repository import GradingTermRepository
from rest_framework.exceptions import NotFound

class UpdateGradingTermService:
    def __init__(self, grading_term_repository: GradingTermRepository):
        self.grading_term_repository = grading_term_repository

    def execute(self, grading_term_id: int, gradingSystem_id, academicYear_id, name, order, weight):
        if not self.grading_term_repository.exist_by_id(grading_term_id):
            raise NotFound("Grading term not found")
        grading_term = GradingTerm(
            id=grading_term_id,
            gradingSystem_id=gradingSystem_id,
            academicYear_id=academicYear_id,
            name=name,
            order=order,
            weight=weight,
        )
        return self.grading_term_repository.update(grading_term)
