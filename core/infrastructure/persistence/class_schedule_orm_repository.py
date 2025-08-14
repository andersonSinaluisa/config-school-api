from core.domain.entities.class_schedule import ClassSchedule
from core.domain.repositories.class_schedule_repository import ClassScheduleRepository
from core.models import ClassScheduleModel
from django.utils import timezone


class ClassScheduleOrmRepository(ClassScheduleRepository):

    def all(self):
        schedules = ClassScheduleModel.objects.filter(deleted=False).order_by('id')
        return [ClassSchedule(
            id=schedule.id,
            course_id=schedule.course.id,
            parallel_id=schedule.parallel.id,
            school_year_id=schedule.schoolYear.id,
            subject_id=schedule.subject.id,
            day_of_week=schedule.dayOfWeek,
            start_time=schedule.startTime,
            end_time=schedule.endTime,
            course=schedule.course,
            parallel=schedule.parallel,
            school_year=schedule.schoolYear,
            subject=schedule.subject,
        ) for schedule in schedules]

    def get(self, schedule_id):
        schedule = ClassScheduleModel.objects.get(id=schedule_id, deleted=False)
        return ClassSchedule(
            id=schedule.id,
            course_id=schedule.course.id,
            parallel_id=schedule.parallel.id,
            school_year_id=schedule.schoolYear.id,
            subject_id=schedule.subject.id,
            day_of_week=schedule.dayOfWeek,
            start_time=schedule.startTime,
            end_time=schedule.endTime,
            course=schedule.course,
            parallel=schedule.parallel,
            school_year=schedule.schoolYear,
            subject=schedule.subject,
        )

    def create(self, schedule: ClassSchedule) -> ClassSchedule:
        schedule_model = ClassScheduleModel.objects.create(
            course_id=schedule.course_id,
            parallel_id=schedule.parallel_id,
            schoolYear_id=schedule.school_year_id,
            subject_id=schedule.subject_id,
            dayOfWeek=schedule.day_of_week,
            startTime=schedule.start_time,
            endTime=schedule.end_time,
        )
        return ClassSchedule(
            id=schedule_model.id,
            course_id=schedule_model.course.id,
            parallel_id=schedule_model.parallel.id,
            school_year_id=schedule_model.schoolYear.id,
            subject_id=schedule_model.subject.id,
            day_of_week=schedule_model.dayOfWeek,
            start_time=schedule_model.startTime,
            end_time=schedule_model.endTime,
        )

    def update(self, schedule: ClassSchedule) -> ClassSchedule:
        schedule_model = ClassScheduleModel.objects.get(id=schedule.id, deleted=False)
        schedule_model.course_id = schedule.course_id
        schedule_model.parallel_id = schedule.parallel_id
        schedule_model.schoolYear_id = schedule.school_year_id
        schedule_model.subject_id = schedule.subject_id
        schedule_model.dayOfWeek = schedule.day_of_week
        schedule_model.startTime = schedule.start_time
        schedule_model.endTime = schedule.end_time
        schedule_model.save()
        return ClassSchedule(
            id=schedule_model.id,
            course_id=schedule_model.course.id,
            parallel_id=schedule_model.parallel.id,
            school_year_id=schedule_model.schoolYear.id,
            subject_id=schedule_model.subject.id,
            day_of_week=schedule_model.dayOfWeek,
            start_time=schedule_model.startTime,
            end_time=schedule_model.endTime,
        )

    def delete(self, schedule_id):
        schedule_model = ClassScheduleModel.objects.get(id=schedule_id, deleted=False)
        schedule_model.deleted = True
        schedule_model.deleted_at = timezone.now()
        schedule_model.save()
        return True

    def exist_by_id(self, schedule_id: int) -> bool:
        return ClassScheduleModel.objects.filter(id=schedule_id, deleted=False).exists()

    def exist_by_parallel_day_time(self, parallel_id, day_of_week, start_time) -> bool:
        return ClassScheduleModel.objects.filter(
            parallel_id=parallel_id,
            dayOfWeek=day_of_week,
            startTime=start_time,
            deleted=False
        ).exists()

    def filter_by_parallel_and_subject(self, parallel_id: int, subject_id: int):
        schedules = ClassScheduleModel.objects.filter(
            parallel_id=parallel_id,
            subject_id=subject_id,
            deleted=False
        )
        return [ClassSchedule(
            id=schedule.id,
            course_id=schedule.course.id,
            parallel_id=schedule.parallel.id,
            school_year_id=schedule.schoolYear.id,
            subject_id=schedule.subject.id,
            day_of_week=schedule.dayOfWeek,
            start_time=schedule.startTime,
            end_time=schedule.endTime,
            course=schedule.course,
            parallel=schedule.parallel,
            school_year=schedule.schoolYear,
            subject=schedule.subject,
        ) for schedule in schedules]
