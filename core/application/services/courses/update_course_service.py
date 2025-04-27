from core.domain.entities.course import Course
from core.domain.repositories.course_repository import CourseRepository
from core.domain.repositories.level_repository import LevelRepository
from rest_framework.exceptions import ValidationError, NotFound

class UpdateCourseService:
    
    def __init__(self, course_repository: CourseRepository, level_repository: LevelRepository):
        self.course_repository = course_repository
        self.level_repository = level_repository
    def execute(self, course_id, name, description, level_id):
        course = self.course_repository.get(course_id)
        if not course:
            raise NotFound(f"Course with ID {course_id} not found")
        
        if level_id is not None:
            if not self.level_repository.exist_by_id(level_id):
                raise ValidationError(f"Level with ID {level_id} does not exist")


        new_course = Course(
            id=course_id,
            name=name,
            description=description,
            level_id=level_id
        )
        
        self.course_repository.update(new_course)
        return course