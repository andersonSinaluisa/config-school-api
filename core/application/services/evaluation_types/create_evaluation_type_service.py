from core.domain.entities.evaluation_type import EvaluationType
from core.domain.repositories.evaluation_type_repository import EvaluationTypeRepository
from rest_framework.exceptions import ValidationError

class CreateEvaluationTypeService:
    def __init__(self, evaluation_type_repository: EvaluationTypeRepository):
        self.evaluation_type_repository = evaluation_type_repository

    def execute(self, name, description, weight):
        if self.evaluation_type_repository.exist_by_name(name):
            raise ValidationError("Evaluation type with this name already exists.")
        evaluation_type = EvaluationType(
            id=None,
            name=name,
            description=description,
            weight=weight,
        )
        return self.evaluation_type_repository.create(evaluation_type)
