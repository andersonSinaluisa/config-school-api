from core.models  import ClassScheduleModel
from core.domain.entities.class_schedule import ClassSchedule
def class_schedule_from_model( schedule: ClassScheduleModel) -> ClassSchedule:
    return ClassSchedule(
        id=schedule.id,
        course_id=schedule.course_id,
        parallel_id=schedule.parallel_id,
        school_year_id=schedule.schoolYear_id,
        subject_id=schedule.subject_id,
        day_of_week=schedule.dayOfWeek,
        start_time=schedule.startTime,
        end_time=schedule.endTime,
        course=schedule.course,
        parallel=schedule.parallel,
        school_year=schedule.schoolYear,
        subject=schedule.subject,
    )
