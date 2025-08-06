from core.domain.repositories.evaluation_type_repository import EvaluationTypeRepository
from rest_framework.exceptions import NotFound

class DeleteEvaluationTypeService:
    def __init__(self, evaluation_type_repository: EvaluationTypeRepository):
        self.evaluation_type_repository = evaluation_type_repository

    def execute(self, evaluation_type_id: int):
        if not self.evaluation_type_repository.exist_by_id(evaluation_type_id):
            raise NotFound("Evaluation type not found")
        return self.evaluation_type_repository.delete(evaluation_type_id)
