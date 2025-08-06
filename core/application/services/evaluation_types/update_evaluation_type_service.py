from core.domain.entities.evaluation_type import EvaluationType
from core.domain.repositories.evaluation_type_repository import EvaluationTypeRepository
from rest_framework.exceptions import NotFound

class UpdateEvaluationTypeService:
    def __init__(self, evaluation_type_repository: EvaluationTypeRepository):
        self.evaluation_type_repository = evaluation_type_repository

    def execute(self, evaluation_type_id: int, name, description, weight):
        if not self.evaluation_type_repository.exist_by_id(evaluation_type_id):
            raise NotFound("Evaluation type not found")
        evaluation_type = EvaluationType(
            id=evaluation_type_id,
            name=name,
            description=description,
            weight=weight,
        )
        return self.evaluation_type_repository.update(evaluation_type)
