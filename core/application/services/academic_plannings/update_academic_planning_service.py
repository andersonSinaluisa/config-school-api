from core.domain.entities.academic_planning import AcademicPlanning
from core.domain.repositories.academic_planning_repository import AcademicPlanningRepository
from core.domain.repositories.course_repository import CourseRepository
from core.domain.repositories.parallel_repository import ParallelRepository
from core.domain.repositories.school_year_repository import SchoolYearRepository
from core.domain.repositories.subject_repository import SubjectRepository
from rest_framework.exceptions import ValidationError


class UpdateAcademicPlanningService:
    def __init__(
        self,
        academic_planning_repository: AcademicPlanningRepository,
        course_repository: CourseRepository,
        parallel_repository: ParallelRepository,
        school_year_repository: SchoolYearRepository,
        subject_repository: SubjectRepository,
    ):
        self.academic_planning_repository = academic_planning_repository
        self.course_repository = course_repository
        self.parallel_repository = parallel_repository
        self.school_year_repository = school_year_repository
        self.subject_repository = subject_repository

    def execute(
        self,
        planning_id,
        course_id,
        parallel_id,
        school_year_id,
        subject_id,
        topic,
        start_date,
        end_date,
        description=''
    ):
        if not self.academic_planning_repository.exist_by_id(planning_id):
            raise ValidationError("Academic planning does not exist", code="invalid_planning")
        if not self.course_repository.exist_by_id(course_id):
            raise ValidationError("Course does not exist", code="invalid_course")
        if not self.parallel_repository.exist_by_id(parallel_id):
            raise ValidationError("Parallel does not exist", code="invalid_parallel")
        if not self.school_year_repository.exist_by_id(school_year_id):
            raise ValidationError("School Year does not exist", code="invalid_school_year")
        if not self.subject_repository.exist_by_id(subject_id):
            raise ValidationError("Subject does not exist", code="invalid_subject")
        current = self.academic_planning_repository.get(planning_id)
        if (
            (parallel_id != current.parallel_id or subject_id != current.subject_id or start_date != current.start_date)
            and self.academic_planning_repository.exist_by_parallel_subject_date(parallel_id, subject_id, start_date)
        ):
            raise ValidationError(
                "Planning already exists for this parallel, subject and start date",
                code="duplicate_planning",
            )

        planning = AcademicPlanning(
            id=planning_id,
            course_id=course_id,
            parallel_id=parallel_id,
            school_year_id=school_year_id,
            subject_id=subject_id,
            topic=topic,
            start_date=start_date,
            end_date=end_date,
            description=description,
        )
        return self.academic_planning_repository.update(planning)
