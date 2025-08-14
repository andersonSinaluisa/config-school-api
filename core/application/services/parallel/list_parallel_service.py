



from core.domain.repositories.parallel_repository import ParallelRepository


class ListParallelService:
    def __init__(self, parallel_repository:ParallelRepository):
        self.parallel_repository = parallel_repository

    def execute(self,
        course_id=None,
        school_year_id=None,
        name=None,
        capacity=None,
        section_id=None
    ):
        """
        Returns parallels based on optional filters.
        If no filters are provided, returns all parallels.
        """
        filters = {
            "course_id": course_id,
            "school_year_id": school_year_id,
            "name__icontains": name,  # example of partial search
            "capacity": capacity,
            "section_id": section_id
        }
        # remove None values
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.parallel_repository.find_by_filter(**filters)