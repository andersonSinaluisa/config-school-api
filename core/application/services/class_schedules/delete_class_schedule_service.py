from core.domain.repositories.class_schedule_repository import ClassScheduleRepository
from rest_framework.exceptions import NotFound


class DeleteClassScheduleService:
    def __init__(self, class_schedule_repository: ClassScheduleRepository):
        self.class_schedule_repository = class_schedule_repository

    def execute(self, schedule_id):
        if not self.class_schedule_repository.exist_by_id(schedule_id):
            raise NotFound("Class schedule not found")
        return self.class_schedule_repository.delete(schedule_id)

