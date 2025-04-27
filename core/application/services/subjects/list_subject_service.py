# -*- coding: utf-8 -*-
from core.domain.repositories.subject_repository import SubjectRepository
from rest_framework.exceptions import ValidationError, NotFound
import logging
class ListSubjectService:
    def __init__(self, subject_repository:SubjectRepository):
        self.subject_repository = subject_repository


    def execute(self):
        """
        List all subjects.
        Returns:
            list: A list of subject objects.
        """
        return self.subject_repository.all()