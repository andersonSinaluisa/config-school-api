from dataclasses import dataclass

@dataclass
class Course:
    id: int
    name:str
    level_id:int
    description:str
    
    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.level_id:
            raise ValueError("Level ID cannot be empty")
        if not self.description:
            raise ValueError("Description cannot be empty")