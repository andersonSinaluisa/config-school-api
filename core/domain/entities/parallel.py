from dataclasses import dataclass

from core.domain.entities.course import Course
from core.domain.entities.school_year import SchoolYear
from core.domain.entities.section import Section

@dataclass
class Parallel:
    id: int
    name: str
    course_id: int
    capacity: int
    section_id: int
    school_year_id:int
    course :Course = None
    section :Section = None
    school_year:SchoolYear = None
    
    def __str__(self):
        return self.name.__str__()

    
    def __repr__(self):
        return self.name.__repr__()
    
    
    def __post_init__(self):
        
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not isinstance(self.capacity, int) or self.capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        if not isinstance(self.section_id, int) or self.section_id < 0:
            raise ValueError("Section ID must be a non-negative integer")
        if not isinstance(self.course_id, int) or self.course_id < 0:
            raise ValueError("Course ID must be a non-negative integer")
        if not isinstance(self.school_year_id, int) or self.school_year_id < 0:
            raise ValueError("School Year ID must be a non-negative integer")