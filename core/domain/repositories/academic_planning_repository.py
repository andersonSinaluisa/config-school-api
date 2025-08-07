from abc import ABC, abstractmethod
from datetime import date
from typing import List

from core.domain.entities.academic_planning import AcademicPlanning


class AcademicPlanningRepository(ABC):

    @abstractmethod
    def create(self, planning: AcademicPlanning) -> AcademicPlanning:
        pass

    @abstractmethod
    def all(self) -> List[AcademicPlanning]:
        pass

    @abstractmethod
    def get(self, planning_id: int) -> AcademicPlanning:
        pass

    @abstractmethod
    def update(self, planning: AcademicPlanning) -> AcademicPlanning:
        pass

    @abstractmethod
    def delete(self, planning_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, planning_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_parallel_subject_date(
        self, parallel_id: int, subject_id: int, start_date: date
    ) -> bool:
        pass
