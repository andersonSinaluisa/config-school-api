from abc import ABC, abstractmethod
from datetime import time
from typing import List

from core.domain.entities.class_schedule import ClassSchedule


class ClassScheduleRepository(ABC):

    @abstractmethod
    def create(self, schedule: ClassSchedule) -> ClassSchedule:
        pass

    @abstractmethod
    def all(self) -> List[ClassSchedule]:
        pass

    @abstractmethod
    def get(self, schedule_id: int) -> ClassSchedule:
        pass

    @abstractmethod
    def update(self, schedule: ClassSchedule) -> ClassSchedule:
        pass

    @abstractmethod
    def delete(self, schedule_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, schedule_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_parallel_day_time(self, parallel_id: int, day_of_week: str, start_time: time) -> bool:
        pass

