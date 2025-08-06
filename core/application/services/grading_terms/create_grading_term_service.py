from core.domain.entities.grading_term import GradingTerm
from core.domain.repositories.grading_term_repository import GradingTermRepository

class CreateGradingTermService:
    def __init__(self, grading_term_repository: GradingTermRepository):
        self.grading_term_repository = grading_term_repository

    def execute(self, gradingSystem_id, academicYear_id, name, order, weight):
        grading_term = GradingTerm(
            id=None,
            gradingSystem_id=gradingSystem_id,
            academicYear_id=academicYear_id,
            name=name,
            order=order,
            weight=weight,
        )
        return self.grading_term_repository.create(grading_term)
