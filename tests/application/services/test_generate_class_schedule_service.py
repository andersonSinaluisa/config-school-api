from datetime import time, date
from django.test import TestCase

from core.application.services.class_schedules.generate_class_schedule_service import GenerateClassScheduleService
from core.domain.entities.class_schedule import ClassSchedule
from core.models import (
    CourseModel,
    SubjectModel,
    ParallelModel,
    SectionModel,
    SchoolYearModel,
    CourseSubjectModel,
    LevelModel,
)

# ==== Mappers simples para el test ====
from core.domain.entities.course import Course
from core.domain.entities.section import Section
from core.domain.entities.school_year import SchoolYear
from core.domain.entities.parallel import Parallel
from core.domain.entities.subject import Subject
from core.domain.entities.couse_subject import CourseSubject

from core.application.mappers.course_subject_mapper import course_subject_model_to_entity
from core.application.mappers.parallel_mapper import parallel_model_to_entity
from core.application.mappers.school_year_mapper import school_year_model_to_entity




# ==== TestCase con repositorios fake que devuelven entidades ====
class GenerateClassScheduleServiceTest(TestCase):

    def setUp(self):
        # Crear datos reales en DB
        self.school_year = SchoolYearModel.objects.create(
            name="2025",
            startDate=date(2025, 1, 1),
            endDate=date(2025, 12, 31),
            status="planning",
        )

        self.level = LevelModel.objects.create(
            name="Level 1",
            description="Test level",
            order=1,
        )
        self.course = CourseModel.objects.create(
            name="Course A",
            level=self.level,
            description="Test course",
        )

        self.section = SectionModel.objects.create(
            name="Morning Section",
            type="morning",
            startDate=time(8, 0),
            endDate=time(12, 0),
            days="monday,tuesday,wednesday,thursday,friday",
        )

        self.parallel = ParallelModel.objects.create(
            name="Parallel 1",
            course=self.course,
            capacity=30,
            section=self.section,
            schoolYear=self.school_year,
        )

        self.subject1 = SubjectModel.objects.create(
            name="Math",
            code="MATH101",
            hoursPerWeek=2,
        )
        self.subject2 = SubjectModel.objects.create(
            name="History",
            code="HIST101",
            hoursPerWeek=3,
        )

        CourseSubjectModel.objects.create(
            course=self.course,
            subject=self.subject1,
            hoursPerWeek="02:00:00",
            isRequired=True,
        )
        CourseSubjectModel.objects.create(
            course=self.course,
            subject=self.subject2,
            hoursPerWeek="03:00:00",
            isRequired=True,
        )

        # Repositorios fake con mapper
        class ParallelRepo:
            def get(_, id):
                model = ParallelModel.objects.filter(id=id).select_related(
                    "course", "section", "schoolYear"
                ).first()
                return parallel_model_to_entity(model) if model else None

        class CourseSubjectRepo:
            def get_by_course(_, course_id):
                qs = CourseSubjectModel.objects.filter(
                    course_id=course_id).select_related("subject")
                return [course_subject_model_to_entity(m) for m in qs]

        self.service = GenerateClassScheduleService(
            ParallelRepo(), CourseSubjectRepo())

    def test_generate_schedule_success(self):
        schedules = self.service.execute(self.parallel.id)

        self.assertIsInstance(schedules, list)
        self.assertTrue(all(isinstance(s, ClassSchedule) for s in schedules))

        # total horas = 2 + 3 = 5
        self.assertEqual(len(schedules), 5)

        subjects = [s.subject.name for s in schedules]
        self.assertIn("Math", subjects)
        self.assertIn("History", subjects)

    def test_generate_schedule_parallel_not_found(self):
        class ParallelRepoEmpty:
            def get(_, id): return None

        class CourseSubjectRepoEmpty:
            def get_by_course(_, course_id): return []

        service = GenerateClassScheduleService(
            ParallelRepoEmpty(), CourseSubjectRepoEmpty()
        )

        with self.assertRaises(ValueError, msg="Parallel not found"):
            service.execute(999)
