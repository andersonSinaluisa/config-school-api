from core.domain.repositories.class_schedule_repository import ClassScheduleRepository


class ListClassScheduleService:
    def __init__(self, class_schedule_repository: ClassScheduleRepository):
        self.class_schedule_repository = class_schedule_repository

    def execute(
        self,
        course_id: int = None,
        parallel_id: int = None,
        school_year_id: int = None,
        subject_id: int = None,
        day_of_week: str = None,
    ):
        filters = {
            "course_id": course_id,
            "parallel_id": parallel_id,
            "schoolYear_id": school_year_id,
            "subject_id": subject_id,
            "dayOfWeek": day_of_week,
        }
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.class_schedule_repository.find_by_filter(**filters)

