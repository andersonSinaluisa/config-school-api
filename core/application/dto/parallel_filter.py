from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ParallelFilter:
    course_id: Optional[str] = None
    school_year_id: Optional[str] = None
    name_contains: Optional[str] = None
    is_active: Optional[bool] = None

class ListParallelService:
    def __init__(self, parallel_repository):
        self.parallel_repository = parallel_repository

    def execute(self, flt: ParallelFilter):
        return self.parallel_repository.find_by_filter(flt)
