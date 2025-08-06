from dataclasses import dataclass

@dataclass
class MeetingType:
    id: int
    name: str
    description: str | None

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
