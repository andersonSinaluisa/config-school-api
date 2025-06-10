from dataclasses import dataclass

from core.domain.entities.course import Course
from core.domain.entities.subject import Subject
import datetime
@dataclass
class CourseSubject:
    id: int
    courseId: int
    subjectId: int
    hoursPerWeek: datetime.time
    isRequired: bool
    course: Course = None
    subject: Subject= None
    def __post_init__(self):
        if not self.courseId:
            raise ValueError("Course ID cannot be empty")
        if not self.subjectId:
            raise ValueError("Subject ID cannot be empty")
        if not self.hoursPerWeek:
            raise ValueError("Hours per week cannot be empty")

        if self.hoursPerWeek < datetime.time(0, 0):
            raise ValueError("Hours per week cannot be negative")
        