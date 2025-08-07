from core.domain.repositories.class_schedule_repository import ClassScheduleRepository


class ListClassScheduleService:
    def __init__(self, class_schedule_repository: ClassScheduleRepository):
        self.class_schedule_repository = class_schedule_repository

    def execute(self):
        return self.class_schedule_repository.all()

