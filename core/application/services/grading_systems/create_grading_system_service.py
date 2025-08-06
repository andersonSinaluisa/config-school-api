from core.domain.entities.grading_system import GradingSystem
from core.domain.repositories.grading_system_repository import GradingSystemRepository
from rest_framework.exceptions import ValidationError

class CreateGradingSystemService:
    def __init__(self, grading_system_repository: GradingSystemRepository):
        self.grading_system_repository = grading_system_repository

    def execute(self, name, description, numberOfTerms, passingScore):
        if self.grading_system_repository.exist_by_name(name):
            raise ValidationError("Grading system with this name already exists.")
        grading_system = GradingSystem(
            id=None,
            name=name,
            description=description,
            numberOfTerms=numberOfTerms,
            passingScore=passingScore,
        )
        return self.grading_system_repository.create(grading_system)
