from abc import ABC, abstractmethod
from core.domain.entities.meeting_type import MeetingType

class MeetingTypeRepository(ABC):

    @abstractmethod
    def get(self, meeting_type_id: int) -> MeetingType:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, meeting_type: MeetingType) -> MeetingType:
        pass

    @abstractmethod
    def update(self, meeting_type: MeetingType) -> MeetingType:
        pass

    @abstractmethod
    def delete(self, meeting_type_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, meeting_type_id: int) -> bool:
        pass
