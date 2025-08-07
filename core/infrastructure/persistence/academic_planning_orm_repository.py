from core.domain.entities.academic_planning import AcademicPlanning
from core.domain.repositories.academic_planning_repository import AcademicPlanningRepository
from core.models import AcademicPlanningModel
from django.utils import timezone


class AcademicPlanningOrmRepository(AcademicPlanningRepository):

    def all(self):
        plannings = AcademicPlanningModel.objects.filter(deleted=False).order_by('id')
        return [
            AcademicPlanning(
                id=p.id,
                course_id=p.course.id,
                parallel_id=p.parallel.id,
                school_year_id=p.schoolYear.id,
                subject_id=p.subject.id,
                topic=p.topic,
                start_date=p.startDate,
                end_date=p.endDate,
                description=p.description or '',
                course=p.course,
                parallel=p.parallel,
                school_year=p.schoolYear,
                subject=p.subject,
            )
            for p in plannings
        ]

    def get(self, planning_id):
        p = AcademicPlanningModel.objects.get(id=planning_id, deleted=False)
        return AcademicPlanning(
            id=p.id,
            course_id=p.course.id,
            parallel_id=p.parallel.id,
            school_year_id=p.schoolYear.id,
            subject_id=p.subject.id,
            topic=p.topic,
            start_date=p.startDate,
            end_date=p.endDate,
            description=p.description or '',
            course=p.course,
            parallel=p.parallel,
            school_year=p.schoolYear,
            subject=p.subject,
        )

    def create(self, planning: AcademicPlanning) -> AcademicPlanning:
        model = AcademicPlanningModel.objects.create(
            course_id=planning.course_id,
            parallel_id=planning.parallel_id,
            schoolYear_id=planning.school_year_id,
            subject_id=planning.subject_id,
            topic=planning.topic,
            startDate=planning.start_date,
            endDate=planning.end_date,
            description=planning.description,
        )
        return AcademicPlanning(
            id=model.id,
            course_id=model.course.id,
            parallel_id=model.parallel.id,
            school_year_id=model.schoolYear.id,
            subject_id=model.subject.id,
            topic=model.topic,
            start_date=model.startDate,
            end_date=model.endDate,
            description=model.description or '',
        )

    def update(self, planning: AcademicPlanning) -> AcademicPlanning:
        model = AcademicPlanningModel.objects.get(id=planning.id, deleted=False)
        model.course_id = planning.course_id
        model.parallel_id = planning.parallel_id
        model.schoolYear_id = planning.school_year_id
        model.subject_id = planning.subject_id
        model.topic = planning.topic
        model.startDate = planning.start_date
        model.endDate = planning.end_date
        model.description = planning.description
        model.save()
        return AcademicPlanning(
            id=model.id,
            course_id=model.course.id,
            parallel_id=model.parallel.id,
            school_year_id=model.schoolYear.id,
            subject_id=model.subject.id,
            topic=model.topic,
            start_date=model.startDate,
            end_date=model.endDate,
            description=model.description or '',
        )

    def delete(self, planning_id):
        model = AcademicPlanningModel.objects.get(id=planning_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_id(self, planning_id: int) -> bool:
        return AcademicPlanningModel.objects.filter(id=planning_id, deleted=False).exists()

    def exist_by_parallel_subject_date(self, parallel_id, subject_id, start_date) -> bool:
        return AcademicPlanningModel.objects.filter(
            parallel_id=parallel_id,
            subject_id=subject_id,
            startDate=start_date,
            deleted=False,
        ).exists()
