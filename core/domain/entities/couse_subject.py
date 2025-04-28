from dataclasses import dataclass

from core.domain.entities.course import Course

@dataclass
class CourseSubject:
    id: int
    courseId: int
    subjectId: int
    hoursPerWeek: int
    isRequired: bool
    course: Course = None
    
    def __post_init__(self):
        if not self.courseId:
            raise ValueError("Course ID cannot be empty")
        if not self.subjectId:
            raise ValueError("Subject ID cannot be empty")
        if not self.hoursPerWeek:
            raise ValueError("Hours per week cannot be empty")

        if self.hoursPerWeek < 0:
            raise ValueError("Hours per week cannot be negative")
        