from core.domain.repositories.attendance_code_repository import AttendanceCodeRepository
from rest_framework.exceptions import NotFound

class DeleteAttendanceCodeService:
    def __init__(self, attendance_code_repository: AttendanceCodeRepository):
        self.attendance_code_repository = attendance_code_repository

    def execute(self, attendance_code_id: int):
        if not self.attendance_code_repository.exist_by_id(attendance_code_id):
            raise NotFound("Attendance code not found")
        return self.attendance_code_repository.delete(attendance_code_id)
