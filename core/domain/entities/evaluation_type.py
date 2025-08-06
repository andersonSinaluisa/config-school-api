from dataclasses import dataclass

@dataclass
class EvaluationType:
    id: int
    name: str
    description: str | None
    weight: float

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.weight is None:
            raise ValueError("Weight is required")
