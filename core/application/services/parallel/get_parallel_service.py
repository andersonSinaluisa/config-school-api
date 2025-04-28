

from core.domain.repositories.parallel_repository import ParallelRepository
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

class GetParallelService:
    
    def __init__(self, parallel_repository:ParallelRepository):
        self.parallel_repository = parallel_repository
        
    def execute(self, parallel_id):
        """
        Execute the retrieval of a parallel record by its ID.
        :param parallel_id: The ID of the parallel record to retrieve.
        :return: The retrieved parallel record.
        """
        try:
        # Retrieve the parallel record by its ID
            parallel = self.parallel_repository.get(parallel_id)
        
        
            return parallel
        
        except ObjectDoesNotExist:
            raise NotFound("The parallel record does not exist.", code="parallel_not_found")
        except Exception as e:
            raise NotFound("An error occurred while retrieving the parallel record.", code="parallel_retrieval_error") from e