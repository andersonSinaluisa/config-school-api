from core.domain.repositories.academic_planning_repository import AcademicPlanningRepository
from rest_framework.exceptions import NotFound


class GetAcademicPlanningService:
    def __init__(self, academic_planning_repository: AcademicPlanningRepository):
        self.academic_planning_repository = academic_planning_repository

    def execute(self, planning_id):
        if not self.academic_planning_repository.exist_by_id(planning_id):
            raise NotFound('Academic planning not found')
        return self.academic_planning_repository.get(planning_id)
