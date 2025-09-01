from abc import ABC, abstractmethod
from typing import List

from core.domain.entities.section_break import SectionBreak


class SectionBreakRepository(ABC):
    @abstractmethod
    def all(self, *, section_id: int | None = None) -> List[SectionBreak]:
        pass

    @abstractmethod
    def get(self, section_break_id: int) -> SectionBreak:
        pass

    @abstractmethod
    def create(self, section_break: SectionBreak) -> SectionBreak:
        pass

    @abstractmethod
    def update(self, section_break: SectionBreak) -> SectionBreak:
        pass

    @abstractmethod
    def delete(self, section_break_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, section_break_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_section_day_time(self, section_id: int, day: str, start_time) -> bool:
        pass

