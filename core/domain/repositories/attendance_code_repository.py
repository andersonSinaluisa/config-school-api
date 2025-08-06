from abc import ABC, abstractmethod
from core.domain.entities.attendance_code import AttendanceCode

class AttendanceCodeRepository(ABC):

    @abstractmethod
    def get(self, attendance_code_id: int) -> AttendanceCode:
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def create(self, attendance_code: AttendanceCode) -> AttendanceCode:
        pass

    @abstractmethod
    def update(self, attendance_code: AttendanceCode) -> AttendanceCode:
        pass

    @abstractmethod
    def delete(self, attendance_code_id: int) -> bool:
        pass

    @abstractmethod
    def exist_by_code(self, code: str) -> bool:
        pass

    @abstractmethod
    def exist_by_id(self, attendance_code_id: int) -> bool:
        pass
