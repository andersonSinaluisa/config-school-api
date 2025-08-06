from dataclasses import dataclass

@dataclass
class AttendanceCode:
    id: int
    code: str
    description: str
    affectsGrade: bool

    def __post_init__(self):
        if not self.code:
            raise ValueError("Code cannot be empty")
        if not self.description:
            raise ValueError("Description cannot be empty")
