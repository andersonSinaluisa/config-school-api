from core.domain.repositories.academic_planning_repository import AcademicPlanningRepository


class ListAcademicPlanningService:
    def __init__(self, academic_planning_repository: AcademicPlanningRepository):
        self.academic_planning_repository = academic_planning_repository

    def execute(self):
        return self.academic_planning_repository.all()
