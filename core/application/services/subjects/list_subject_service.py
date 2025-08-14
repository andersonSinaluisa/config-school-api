# -*- coding: utf-8 -*-
from core.domain.repositories.subject_repository import SubjectRepository


class ListSubjectService:
    def __init__(self, subject_repository: SubjectRepository):
        self.subject_repository = subject_repository

    def execute(self, name: str = None, code: str = None):
        """
        List subjects applying optional filters.

        Args:
            name (str, optional): Filter by subject name (partial match).
            code (str, optional): Filter by subject code (partial match).

        Returns:
            list: A list of subject objects.
        """
        filters = {
            "name__icontains": name,
            "code__icontains": code,
        }
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.subject_repository.find_by_filter(**filters)