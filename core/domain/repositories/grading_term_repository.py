from abc import ABC, abstractmethod
from core.domain.entities.grading_term import GradingTerm

class GradingTermRepository(ABC):

    @abstractmethod
    def get(self, grading_term_id: int) -> GradingTerm:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, grading_term: GradingTerm) -> GradingTerm:
        pass

    @abstractmethod
    def update(self, grading_term: GradingTerm) -> GradingTerm:
        pass

    @abstractmethod
    def delete(self, grading_term_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, grading_term_id: int) -> bool:
        pass
