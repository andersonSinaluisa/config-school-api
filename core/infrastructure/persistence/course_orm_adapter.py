# -*- coding: utf-8 -*-
"""
Course ORM Adapter for interacting with the CourseModel.
"""
from operator import le

from django.utils import timezone
from core.domain.repositories.course_repository import CourseRepository
from core.models import CourseModel
from core.domain.entities.course import Course
class CourseORMAdapter(CourseRepository):
    """Course ORM Adapter for interacting with the CourseModel."""

    def get(self, course_id: str):
        course = CourseModel.objects.get(id=course_id, deleted=False)
        return Course(
            id=course.id,
            name=course.name,
            level_id=course.level.id,
            description=course.description,
            level=course.level
        )
    def all(self):
        return [Course(
            id=course.id,
            name=course.name,
            level_id=course.level.id,
            description=course.description,
            level=course.level
        ) for course in CourseModel.objects.filter(deleted=False).order_by('id')]

    def create(self, course):
        return CourseModel.objects.create(
            name=course.name,
            level_id=course.level_id,
            description=course.description
        )
        
    def update(self, course):
        CourseModel.objects.filter(id=course.id, deleted=False).update(
            name=course.name,
            level_id=course.level_id,
            description=course.description
        )
        return CourseModel.objects.get(id=course.id)

    def delete(self, course_id: str):
        course = CourseModel.objects.get(id=course_id, deleted=False)
        course.deleted = True
        course.deleted_at = timezone.now()
        course.save()
        return course
    
    
    def exist_by_name(self, name: str) -> bool:
        return CourseModel.objects.filter(name=name, deleted=False).exists()
    
    
    def exist_by_id(self, course_id: str) -> bool:
        return CourseModel.objects.filter(id=course_id, deleted=False).exists()