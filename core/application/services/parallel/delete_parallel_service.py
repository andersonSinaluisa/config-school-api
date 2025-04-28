
from core.domain.repositories.parallel_repository import ParallelRepository
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError

class DeleteParallelService:
    
    def __init__(self, parallel_repository:ParallelRepository):
        self.parallel_repository = parallel_repository
        
        
    def execute(self, parallel_id:int) -> None:
        """
        Delete a parallel by its ID.
        
        :param parallel_id: The ID of the parallel to delete.
        :return: None
        """
        try:
            # Check if the parallel exists before attempting to delete it
            self.parallel_repository.delete(parallel_id)
        except ObjectDoesNotExist:
            raise NotFound("Parallel not found.")
            