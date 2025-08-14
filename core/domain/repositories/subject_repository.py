# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List, Optional

from core.domain.entities.subject import Subject


class SubjectRepository(ABC):
    
    @abstractmethod
    def create(self, subject_data: Subject) -> Subject:
        """
        Create a new subject.
        Args:
            subject_data (dict): A dictionary containing subject data.
        Returns:
            dict: The created subject object.
        """
        pass

    @abstractmethod
    def all(self) -> List[Subject]:
        """
        List all subjects.
        Returns:
            List[dict]: A list of subject objects.
        """
        pass

    @abstractmethod
    def get(self, subject_id: int) -> Optional[Subject]:
        """
        Retrieve a subject by its ID.
        Args:
            subject_id (int): The ID of the subject to retrieve.
        Returns:
            Optional[dict]: The subject object if found, None otherwise.
        """
        pass

    @abstractmethod
    def update(self, subject_data: Subject) -> Subject:
        """
        Update a subject by its ID.
        Args:
            subject_id (int): The ID of the subject to update.
            subject_data (dict): A dictionary containing updated subject data.
        Returns:
            dict: The updated subject object.
        """
        pass

    @abstractmethod
    def delete(self, subject_id: int) -> None:
        """
        Delete a subject by its ID.
        Args:
            subject_id (int): The ID of the subject to delete.
        """
        pass
    
    @abstractmethod
    def exist_by_id(self, subject_id: int) -> bool:
        """
        Check if a subject exists by its ID.
        Args:
            subject_id (int): The ID of the subject to check.
        Returns:
            bool: True if the subject exists, False otherwise.
        """
        pass
    
    
    @abstractmethod
    def exist_by_name(self, name: str) -> bool:
        """
        Check if a subject exists by its name.
        Args:
            name (str): The name of the subject to check.
        Returns:
            bool: True if the subject exists, False otherwise.
        """
        pass

    @abstractmethod
    def find_by_filter(self, **filters) -> List[Subject]:
        """Find subjects by the given filter."""
        pass
    
    