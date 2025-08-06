from core.domain.entities.grading_system import GradingSystem
from core.domain.repositories.grading_system_repository import GradingSystemRepository
from rest_framework.exceptions import NotFound

class UpdateGradingSystemService:
    def __init__(self, grading_system_repository: GradingSystemRepository):
        self.grading_system_repository = grading_system_repository

    def execute(self, grading_system_id: int, name, description, numberOfTerms, passingScore):
        if not self.grading_system_repository.exist_by_id(grading_system_id):
            raise NotFound("Grading system not found")
        grading_system = GradingSystem(
            id=grading_system_id,
            name=name,
            description=description,
            numberOfTerms=numberOfTerms,
            passingScore=passingScore,
        )
        return self.grading_system_repository.update(grading_system)
