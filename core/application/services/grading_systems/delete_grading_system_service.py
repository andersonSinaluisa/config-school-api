from core.domain.repositories.grading_system_repository import GradingSystemRepository
from rest_framework.exceptions import NotFound

class DeleteGradingSystemService:
    def __init__(self, grading_system_repository: GradingSystemRepository):
        self.grading_system_repository = grading_system_repository

    def execute(self, grading_system_id: int):
        if not self.grading_system_repository.exist_by_id(grading_system_id):
            raise NotFound("Grading system not found")
        return self.grading_system_repository.delete(grading_system_id)
