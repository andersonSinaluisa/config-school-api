from dataclasses import dataclass
from datetime import time

from core.domain.entities.course import Course
from core.domain.entities.parallel import Parallel
from core.domain.entities.school_year import SchoolYear
from core.domain.entities.subject import Subject


@dataclass
class ClassSchedule:
    id: int
    course_id: int
    parallel_id: int
    school_year_id: int
    subject_id: int
    day_of_week: str
    start_time: time
    end_time: time
    course: Course = None
    parallel: Parallel = None
    school_year: SchoolYear = None
    subject: Subject = None

    def __post_init__(self):
        if not self.day_of_week:
            raise ValueError("Day of week cannot be empty")
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time")

