from dataclasses import dataclass

@dataclass
class GradingSystem:
    id: int
    name: str
    description: str | None
    numberOfTerms: int
    passingScore: float

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.numberOfTerms is None or self.numberOfTerms <= 0:
            raise ValueError("Number of terms must be positive")
