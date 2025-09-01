from dataclasses import dataclass
from datetime import time


@dataclass
class SectionBreak:
    id: int
    section_id: int
    day: str
    start_time: time
    end_time: time

    def __post_init__(self):
        if not self.section_id:
            raise ValueError("section_id is required")
        if not self.day:
            raise ValueError("day is required")
        if self.start_time >= self.end_time:
            raise ValueError("start_time must be before end_time")

