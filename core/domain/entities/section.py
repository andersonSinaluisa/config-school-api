
from dataclasses import dataclass


@dataclass
class Section:
    id: int
    name: str
    type: str
    description: str
