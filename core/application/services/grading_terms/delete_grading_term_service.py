from core.domain.repositories.grading_term_repository import GradingTermRepository
from rest_framework.exceptions import NotFound

class DeleteGradingTermService:
    def __init__(self, grading_term_repository: GradingTermRepository):
        self.grading_term_repository = grading_term_repository

    def execute(self, grading_term_id: int):
        if not self.grading_term_repository.exist_by_id(grading_term_id):
            raise NotFound("Grading term not found")
        return self.grading_term_repository.delete(grading_term_id)
