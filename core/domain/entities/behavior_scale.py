from dataclasses import dataclass

@dataclass
class BehaviorScale:
    id: int
    name: str
    minScore: float
    maxScore: float

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.minScore is None or self.maxScore is None:
            raise ValueError("Scores are required")
