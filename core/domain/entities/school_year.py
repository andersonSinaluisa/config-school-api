from dataclasses import dataclass

from datetime import date



@dataclass
class SchoolYear:
    id: int
    name: str
    startDate: date
    endDate: date
    status: str

    def __str__(self):
        return self.name.__str__()
