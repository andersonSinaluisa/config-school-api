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

    
    def __post_init__(self):
        if not isinstance(self.startDate, date) or not isinstance(self.endDate, date):
            raise ValueError("startDate and endDate must be of type date")
        if self.startDate >= self.endDate:
            raise ValueError("startDate must be before endDate")