


from core.domain.repositories.parallel_repository import ParallelRepository


class ListParallelByCourseService:
    def __init__(self, parallel_repository: ParallelRepository):
        self.parallel_repository = parallel_repository

    def execute(self, course_id: str):
        """
        Retrieves all parallels associated with a specific course.

        :param course_id: The ID of the course for which to retrieve parallels.
        :return: A list of parallels associated with the specified course.
        """
        return self.parallel_repository.find_by_course_id(course_id)