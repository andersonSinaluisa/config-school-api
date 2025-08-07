from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

from core.domain.repositories.class_schedule_repository import ClassScheduleRepository


class GetClassScheduleService:
    def __init__(self, class_schedule_repository: ClassScheduleRepository):
        self.class_schedule_repository = class_schedule_repository

    def execute(self, schedule_id):
        try:
            return self.class_schedule_repository.get(schedule_id)
        except ObjectDoesNotExist:
            raise NotFound("Class schedule not found")

