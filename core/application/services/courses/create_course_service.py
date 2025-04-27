from core.domain.entities.course import Course
from core.domain.repositories.course_repository import CourseRepository
from core.domain.repositories.level_repository import LevelRepository
from rest_framework.exceptions import ValidationError, NotFound

class CreateCourseService:
    def __init__(self, course_repository: CourseRepository,
                    level_repository: LevelRepository):
        """Initialize the service with a course repository.
        Args:
            course_repository (CourseRepository): The repository to interact with course data.
            level_repository (LevelRepository): The repository to interact with level data.
        """
        self.level_repository = level_repository
        self.course_repository = course_repository

    def execute(
        self,
        name: str,
        level_id: int,
        description: str) -> Course:

        
        if self.course_repository.exist_by_name(name):
            raise ValidationError(f"Course with name {name} already exists",
                                  code="course_name_exists")
        
        #TODO: Add validation for level_id 
        if not self.level_repository.exist_by_id(level_id):
            raise NotFound(f"Level with ID {level_id} does not exist",
                           code="level_not_found")
        
        new_course = Course(
            id=None,
            name=name,
            level_id=level_id,
            description=description
        )
        return self.course_repository.create(new_course)