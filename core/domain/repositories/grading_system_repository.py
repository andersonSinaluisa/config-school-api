from abc import ABC, abstractmethod
from core.domain.entities.grading_system import GradingSystem

class GradingSystemRepository(ABC):

    @abstractmethod
    def get(self, grading_system_id: int) -> GradingSystem:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, grading_system: GradingSystem) -> GradingSystem:
        pass

    @abstractmethod
    def update(self, grading_system: GradingSystem) -> GradingSystem:
        pass

    @abstractmethod
    def delete(self, grading_system_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, grading_system_id: int) -> bool:
        pass
