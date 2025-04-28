



from core.domain.repositories.parallel_repository import ParallelRepository


class ListParallelService:
    def __init__(self, parallel_repository:ParallelRepository):
        self.parallel_repository = parallel_repository

    def execute(self):
        return self.parallel_repository.all()