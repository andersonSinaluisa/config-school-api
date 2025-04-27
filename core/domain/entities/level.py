from dataclasses import dataclass

@dataclass
class Level:
    id: int
    name: str
    description: str
    order: int
    
    
    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.description:
            raise ValueError("Description cannot be empty")
        if not isinstance(self.order, int) or self.order < 0:
            raise ValueError("Order must be a non-negative integer")