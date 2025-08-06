from core.domain.entities.attendance_code import AttendanceCode
from core.domain.repositories.attendance_code_repository import AttendanceCodeRepository
from core.models import AttendanceCodeModel
from django.utils import timezone

class AttendanceCodeOrmRepository(AttendanceCodeRepository):
    def get(self, attendance_code_id: int) -> AttendanceCode:
        model = AttendanceCodeModel.objects.get(id=attendance_code_id, deleted=False)
        return AttendanceCode(
            id=model.id,
            code=model.code,
            description=model.description,
            affectsGrade=model.affectsGrade,
        )

    def all(self):
        models = AttendanceCodeModel.objects.filter(deleted=False).order_by('code')
        return [
            AttendanceCode(
                id=m.id,
                code=m.code,
                description=m.description,
                affectsGrade=m.affectsGrade,
            )
            for m in models
        ]

    def create(self, attendance_code: AttendanceCode) -> AttendanceCode:
        model = AttendanceCodeModel(
            code=attendance_code.code,
            description=attendance_code.description,
            affectsGrade=attendance_code.affectsGrade,
        )
        model.save()
        attendance_code.id = model.id
        return attendance_code

    def update(self, attendance_code: AttendanceCode) -> AttendanceCode:
        model = AttendanceCodeModel.objects.get(id=attendance_code.id, deleted=False)
        model.code = attendance_code.code
        model.description = attendance_code.description
        model.affectsGrade = attendance_code.affectsGrade
        model.save()
        return attendance_code

    def delete(self, attendance_code_id: int) -> bool:
        model = AttendanceCodeModel.objects.get(id=attendance_code_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_code(self, code: str) -> bool:
        return AttendanceCodeModel.objects.filter(code=code, deleted=False).exists()

    def exist_by_id(self, attendance_code_id: int) -> bool:
        return AttendanceCodeModel.objects.filter(id=attendance_code_id, deleted=False).exists()
