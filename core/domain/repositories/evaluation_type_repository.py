from abc import ABC, abstractmethod
from core.domain.entities.evaluation_type import EvaluationType

class EvaluationTypeRepository(ABC):

    @abstractmethod
    def get(self, evaluation_type_id: int) -> EvaluationType:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, evaluation_type: EvaluationType) -> EvaluationType:
        pass

    @abstractmethod
    def update(self, evaluation_type: EvaluationType) -> EvaluationType:
        pass

    @abstractmethod
    def delete(self, evaluation_type_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, evaluation_type_id: int) -> bool:
        pass
