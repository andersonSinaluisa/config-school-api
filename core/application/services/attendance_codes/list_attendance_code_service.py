from core.domain.repositories.attendance_code_repository import AttendanceCodeRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListAttendanceCodeService:
    def __init__(self, attendance_code_repository: AttendanceCodeRepository):
        self.attendance_code_repository = attendance_code_repository

    def execute(self):
        try:
            return self.attendance_code_repository.all()
        except Exception as e:
            logging.error(f"Error listing attendance codes: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No attendance codes found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid attendance code data")
            else:
                raise Exception("An unexpected error occurred") from e
