from dataclasses import dataclass

@dataclass
class Parallel:
    id: int
    name: str
    course_id: int
    capacity: int
    section_id: int
    school_year_id:int
    def __str__(self):
        return self.name.__str__()

    
    def __repr__(self):
        return self.name.__repr__()
    
    
    def __post_init__(self):
        self.name = self.name.strip()
        self.course_id = int(self.course_id)
        self.capacity = int(self.capacity)
        self.section_id = int(self.section_id)
        self.school_year_id = int(self.school_year_id)