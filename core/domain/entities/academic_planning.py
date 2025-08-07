from dataclasses import dataclass
from datetime import date

from core.domain.entities.course import Course
from core.domain.entities.parallel import Parallel
from core.domain.entities.school_year import SchoolYear
from core.domain.entities.subject import Subject


@dataclass
class AcademicPlanning:
    id: int
    course_id: int
    parallel_id: int
    school_year_id: int
    subject_id: int
    topic: str
    start_date: date
    end_date: date
    description: str = ''
    course: Course = None
    parallel: Parallel = None
    school_year: SchoolYear = None
    subject: Subject = None

    def __post_init__(self):
        if self.start_date > self.end_date:
            raise ValueError('Start date must be before end date')
