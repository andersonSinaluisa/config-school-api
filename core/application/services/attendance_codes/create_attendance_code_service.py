from core.domain.entities.attendance_code import AttendanceCode
from core.domain.repositories.attendance_code_repository import AttendanceCodeRepository
from rest_framework.exceptions import ValidationError

class CreateAttendanceCodeService:
    def __init__(self, attendance_code_repository: AttendanceCodeRepository):
        self.attendance_code_repository = attendance_code_repository

    def execute(self, code, description, affectsGrade=False):
        if self.attendance_code_repository.exist_by_code(code):
            raise ValidationError("Attendance code with this code already exists.")
        attendance_code = AttendanceCode(
            id=None,
            code=code,
            description=description,
            affectsGrade=affectsGrade,
        )
        return self.attendance_code_repository.create(attendance_code)
