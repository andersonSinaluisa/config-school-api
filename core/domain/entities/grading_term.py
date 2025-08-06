from dataclasses import dataclass

@dataclass
class GradingTerm:
    id: int
    gradingSystem_id: int
    academicYear_id: int
    name: str
    order: int
    weight: float

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.order is None or self.order < 0:
            raise ValueError("Order must be non-negative")
        if self.weight is None:
            raise ValueError("Weight is required")
