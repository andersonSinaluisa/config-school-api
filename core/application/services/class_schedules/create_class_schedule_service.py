from core.domain.entities.class_schedule import ClassSchedule
from core.domain.repositories.class_schedule_repository import ClassScheduleRepository
from core.domain.repositories.course_repository import CourseRepository
from core.domain.repositories.parallel_repository import ParallelRepository
from core.domain.repositories.school_year_repository import SchoolYearRepository
from core.domain.repositories.subject_repository import SubjectRepository
from rest_framework.exceptions import ValidationError
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from core.domain.services.class_schedule_hours_service import ClassScheduleHoursService
from datetime import time, datetime, date, timedelta
class CreateClassScheduleService:
    def __init__(
        self,
        class_schedule_repository: ClassScheduleRepository,
        course_repository: CourseRepository,
        parallel_repository: ParallelRepository,
        school_year_repository: SchoolYearRepository,
        subject_repository: SubjectRepository,
        course_subject_repository: CourseSubjectRepository
    ):
        self.class_schedule_repository = class_schedule_repository
        self.course_repository = course_repository
        self.parallel_repository = parallel_repository
        self.school_year_repository = school_year_repository
        self.subject_repository = subject_repository
        self.course_subject_repository = course_subject_repository

    def execute(
        self,
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
            raise ValidationError(
                "Schedule already exists for this parallel at that time",
                code="duplicate_schedule",
            )
        if not self.course_subject_repository.exist_by_course_and_subject(
                course_id,
                subject_id
        ):
            raise ValidationError("Materia no asignada al curso", code="invalid_course_subject")

        course_subject = self.course_subject_repository.get_by_course_and_subject(
            course_id,
            subject_id
        )

      

        if course_subject.hoursPerWeek <= time(0, 0):
            raise ValidationError(
                "Horas por semana no puede ser cero", code="invalid_course_subject")

        class_based_schedules = self.class_schedule_repository.filter_by_parallel_and_subject(
            parallel_id, subject_id
        )

        # Validar rango de horas antes de cálculos
        if start_time >= end_time:
            raise ValidationError(
                "Start time must be before end time", code="invalid_time_range")

        # Validar acumulado de horas usando el Domain Service
        ClassScheduleHoursService.validate_total_hours(
            start_time,
            end_time,
            class_based_schedules,
            course_subject.hoursPerWeek
        )

        schedule = ClassSchedule(
            id=None,
            course_id=course_id,
            parallel_id=parallel_id,
            school_year_id=school_year_id,
            subject_id=subject_id,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
        )
        return self.class_schedule_repository.create(schedule)

