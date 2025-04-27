from abc import ABC, abstractmethod
from typing import List, Dict, Any

from core.domain.entities.parallel import Parallel
class ParallelRepository(ABC):
    """
    Abstract base class for parallel repositories.
    """

    @abstractmethod
    def all(self) -> List[Parallel]:
        """
        Retrieve all parallel records.
        :return: List of parallel records.
        """
        pass
    
    
    @abstractmethod
    def get(self, parallel_id: str) -> Parallel:
        """
        Retrieve a parallel record by its ID.
        :param parallel_id: The ID of the parallel record to retrieve.
        :return: The parallel record.
        """
        pass
    
    
    @abstractmethod
    def create(self, parallel: Parallel) -> Parallel:
        """
        Create a new parallel record.
        :param parallel: The parallel record to create.
        :return: The created parallel record.
        """
        pass
    
    
    
    @abstractmethod
    def update(self, parallel: Parallel) -> Parallel:
        """
        Update an existing parallel record.
        :param parallel: The parallel record to update.
        :return: The updated parallel record.
        """
        pass
    
    
    @abstractmethod
    def delete(self, parallel_id: str) -> None:
        """
        Delete a parallel record by its ID.
        :param parallel_id: The ID of the parallel record to delete.
        """
        pass
    
    @abstractmethod
    def exist_by_course_id_and_subject_id(self, course_id: str, subject_id: str) -> bool:
        """Check if a course exists by its course ID and subject ID."""
        pass
    
    
    
    
    @abstractmethod
    def find_by_id(self, parallel_id: str) -> Parallel:
        """
        Find a parallel record by its ID.
        :param parallel_id: The ID of the parallel record to find.
        :return: The parallel record.
        """
        pass
    
    
    @abstractmethod
    def exists_by_name(self, name: str) -> bool:
        """
        Check if a parallel record exists by its name.
        :param name: The name of the parallel record to check.
        :return: True if the parallel record exists, False otherwise.
        """
        pass
    
    