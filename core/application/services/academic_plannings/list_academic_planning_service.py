from core.domain.repositories.academic_planning_repository import AcademicPlanningRepository


class ListAcademicPlanningService:
    def __init__(self, academic_planning_repository: AcademicPlanningRepository):
        self.academic_planning_repository = academic_planning_repository

    def execute(
        self,
        course_id: int = None,
        parallel_id: int = None,
        school_year_id: int = None,
        subject_id: int = None,
        topic: str = None,
    ):
        filters = {
            "course_id": course_id,
            "parallel_id": parallel_id,
            "schoolYear_id": school_year_id,
            "subject_id": subject_id,
            "topic__icontains": topic,
        }
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.academic_planning_repository.find_by_filter(**filters)
