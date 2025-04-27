from dataclasses import dataclass

@dataclass
class Subject:
    id: int
    name: str
    code: str
    description: str
    hoursPerWeek: int

    def __str__(self):
        return self.name.__str__()
