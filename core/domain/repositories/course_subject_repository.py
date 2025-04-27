
from abc import ABC, abstractmethod
from typing import List
from core.domain.entities.couse_subject import CourseSubject


class CourseSubjectRepository(ABC):

    @abstractmethod
    def all(self)-> List[CourseSubject]:
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