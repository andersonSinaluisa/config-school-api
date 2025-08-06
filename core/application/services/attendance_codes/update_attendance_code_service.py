from core.domain.entities.attendance_code import AttendanceCode
from core.domain.repositories.attendance_code_repository import AttendanceCodeRepository
from rest_framework.exceptions import NotFound

class UpdateAttendanceCodeService:
    def __init__(self, attendance_code_repository: AttendanceCodeRepository):
        self.attendance_code_repository = attendance_code_repository

    def execute(self, attendance_code_id: int, code, description, affectsGrade=False):
        if not self.attendance_code_repository.exist_by_id(attendance_code_id):
            raise NotFound("Attendance code not found")
        attendance_code = AttendanceCode(
            id=attendance_code_id,
            code=code,
            description=description,
            affectsGrade=affectsGrade,
        )
        return self.attendance_code_repository.update(attendance_code)
