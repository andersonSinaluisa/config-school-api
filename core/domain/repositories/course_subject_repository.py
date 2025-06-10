
from abc import ABC, abstractmethod
from typing import List
from core.domain.entities.couse_subject import CourseSubject


class CourseSubjectRepository(ABC):

    @abstractmethod
    def all(self) -> List[CourseSubject]:
        pass


    @abstractmethod
    def get(self, id)->CourseSubject:
        pass


    @abstractmethod
    def update(self,data:CourseSubject)->CourseSubject:
        pass


    @abstractmethod
    def create(self,data:CourseSubject)->CourseSubject:
        pass


    @abstractmethod
    def delete(self,id:int)->bool:
        pass
        
    @abstractmethod
    def exist_by_course_and_subject(self, course_id:int, subject_id:int)->bool:
        pass
    
    
    @abstractmethod
    def get_by_course(self, course_id:int)->List[CourseSubject]:
        pass
    
    @abstractmethod
    def create_range(self, course_subjects:List[CourseSubject])->List[CourseSubject]:
        """
        Create a range of CourseSubject entities.
        """
        pass
    
    @abstractmethod
    def remove_from_course(self, course_id:int, subject_id:int):
        """
        Remove all CourseSubject entities associated with a given course.
        """
        pass
    
    @abstractmethod
    def remove_range_from_course(self, course_subjects:List[int]):
        """
        Remove a range of CourseSubject entities from a course.
        """
        pass
