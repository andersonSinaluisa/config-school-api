from abc import ABC, abstractmethod
from core.domain.entities.behavior_scale import BehaviorScale

class BehaviorScaleRepository(ABC):

    @abstractmethod
    def get(self, behavior_scale_id: int) -> BehaviorScale:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, behavior_scale: BehaviorScale) -> BehaviorScale:
        pass

    @abstractmethod
    def update(self, behavior_scale: BehaviorScale) -> BehaviorScale:
        pass

    @abstractmethod
    def delete(self, behavior_scale_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, behavior_scale_id: int) -> bool:
        pass
