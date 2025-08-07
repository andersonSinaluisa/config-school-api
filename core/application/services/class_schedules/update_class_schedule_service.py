from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError

from core.domain.entities.class_schedule import ClassSchedule
from core.domain.repositories.class_schedule_repository import ClassScheduleRepository
from core.domain.repositories.course_repository import CourseRepository
from core.domain.repositories.parallel_repository import ParallelRepository
from core.domain.repositories.school_year_repository import SchoolYearRepository
from core.domain.repositories.subject_repository import SubjectRepository


class UpdateClassScheduleService:
    def __init__(
        self,
        class_schedule_repository: ClassScheduleRepository,
        course_repository: CourseRepository,
        parallel_repository: ParallelRepository,
        school_year_repository: SchoolYearRepository,
        subject_repository: SubjectRepository,
    ):
        self.class_schedule_repository = class_schedule_repository
        self.course_repository = course_repository
        self.parallel_repository = parallel_repository
        self.school_year_repository = school_year_repository
        self.subject_repository = subject_repository

    def execute(
        self,
        schedule_id,
        course_id,
        parallel_id,
        school_year_id,
        subject_id,
        day_of_week,
        start_time,
        end_time,
    ):
        if not self.course_repository.exist_by_id(course_id):
            raise ValidationError("Course does not exist", code="invalid_course")
        if not self.parallel_repository.exist_by_id(parallel_id):
            raise ValidationError("Parallel does not exist", code="invalid_parallel")
        if not self.school_year_repository.exist_by_id(school_year_id):
            raise ValidationError("School Year does not exist", code="invalid_school_year")
        if not self.subject_repository.exist_by_id(subject_id):
            raise ValidationError("Subject does not exist", code="invalid_subject")
        if self.class_schedule_repository.exist_by_parallel_day_time(parallel_id, day_of_week, start_time):
            existing = self.class_schedule_repository.get(schedule_id)
            if not (
                existing.parallel_id == parallel_id
                and existing.day_of_week == day_of_week
                and existing.start_time == start_time
            ):
                raise ValidationError(
                    "Schedule already exists for this parallel at that time",
                    code="duplicate_schedule",
                )

        try:
            schedule = ClassSchedule(
                id=schedule_id,
                course_id=course_id,
                parallel_id=parallel_id,
                school_year_id=school_year_id,
                subject_id=subject_id,
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time,
            )
            return self.class_schedule_repository.update(schedule)
        except ObjectDoesNotExist:
            raise NotFound("Class schedule not found", code="schedule_not_found")

