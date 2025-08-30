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
    def get(self, parallel_id: int) -> Parallel:
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
    def delete(self, parallel_id: int) -> None:
        """
        Delete a parallel record by its ID.
        :param parallel_id: The ID of the parallel record to delete.
        """
        pass
    
    @abstractmethod
    def exist_by_course_id_and_section_id(self, course_id: int, subject_id: int) -> bool:
        """Check if a course exists by its course ID and subject ID."""
        pass
    
    @abstractmethod
    def exist_by_course_id_and_section_id_except_id(self, course_id: int, section_id: int, parallel_id: int) -> bool:
        """
        Check if a course exists by its course ID and subject ID except for a specific parallel ID.
        :param course_id: The ID of the course.
        :param section_id: The ID of the section.
        :param parallel_id: The ID of the parallel to exclude from the check.
        :return: True if the course exists, False otherwise.
        """
        pass
    
    @abstractmethod
    def exist_by_id(self, parallel_id: int) -> bool:
        """
        Check if a parallel record exists by its ID.
        :param parallel_id: The ID of the parallel record to check.
        :return: True if the parallel record exists, False otherwise.
        """
        pass
    
    
    
    @abstractmethod
    def find_by_id(self, parallel_id: int) -> Parallel:
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
    
    @abstractmethod
    def find_by_course_id(self, course_id: int) -> List[Parallel]:
        """
        Retrieve all parallels associated with a specific course.
        :param course_id: The ID of the course for which to retrieve parallels.
        :return: A list of parallels associated with the specified course.
        """
        pass
    
    @abstractmethod
    def find_by_filter(self, **filters) -> List[Parallel]:
        """
        Find parallels by the given filter.
        :param filter: The filter to apply.
        :return: A list of parallels matching the filter.
        """
        pass