from datetime import datetime
from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import time, timedelta, date

from core.models import (
    LevelModel, CourseModel, CourseSubjectModel, ParallelModel, SchoolYearModel,
    SectionModel, SubjectModel, LogActivityModel, ConfigurationModel,
    GradingSystemModel, GradingTermModel, EvaluationTypeModel, MeetingTypeModel,
    AttendanceCodeModel, BehaviorScaleModel, ClassScheduleModel, AcademicPlanningModel
)

fake = Faker()


class Command(BaseCommand):
    help = "Crea datos falsos para todos los modelos académicos"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Generando datos falsos..."))

        # ---------- LEVELS ----------
        levels = []
        for i in range(3):
            level = LevelModel.objects.create(
                name=f"Nivel {i+1}",
                description=fake.sentence(),
                order=i+1
            )
            levels.append(level)

        # ---------- COURSES ----------
        courses = []
        for level in levels:
            for i in range(2):
                course = CourseModel.objects.create(
                    name=f"{level.name} - Curso {i+1}",
                    level=level,
                    description=fake.text()
                )
                courses.append(course)

        # ---------- SUBJECTS ----------
        subjects = []
        for i in range(5):
            subject = SubjectModel.objects.create(
                name=fake.word().capitalize(),
                code=f"S{i+1:03}",
                description=fake.text(),
                hoursPerWeek=random.randint(2, 6)
            )
            subjects.append(subject)

        # ---------- COURSE SUBJECTS ----------
        for course in courses:
            for subject in random.sample(subjects, k=3):
                CourseSubjectModel.objects.create(
                    course=course,
                    subject=subject,
                    hoursPerWeek=time(hour=random.randint(1, 3)),
                    isRequired=random.choice([True, False])
                )

        # ---------- SECTIONS ----------
        sections = []
        for name, _ in SectionModel.TYPE_CHOICES:
            sections.append(
                SectionModel.objects.create(
                    name=f"Sección {name.capitalize()}",
                    type=name,
                    description=fake.text(),
                    startDate=time(hour=8),
                    endDate=time(hour=14),
                    hasBreak=random.choice([True, False]),
                    breakCount=random.randint(0, 2),
                    breakDuration=random.randint(0, 30),
                    days="Lunes,Martes,Miércoles,Jueves,Viernes"
                )
            )

        # ---------- SCHOOL YEARS ----------
        school_years = []
        for i in range(2):
            start = date(2024 + i, 1, 15)
            end = date(2024 + i, 12, 15)
            school_years.append(
                SchoolYearModel.objects.create(
                    name=f"Año lectivo {2024 + i}",
                    startDate=start,
                    endDate=end,
                    status=random.choice(
                        [s[0] for s in SchoolYearModel.STATUS_CHOICES])
                )
            )

        # ---------- PARALLELS ----------
        parallels = []
        for course in courses:
            for section in sections:
                parallel = ParallelModel.objects.create(
                    name=f"Paralelo {fake.random_uppercase_letter()}",
                    course=course,
                    capacity=random.randint(20, 40),
                    section=section,
                    schoolYear=random.choice(school_years)
                )
                parallels.append(parallel)

        # ---------- CLASS SCHEDULES ----------
        # ---------- CLASS SCHEDULES ----------


        day_choices = [c[0] for c in ClassScheduleModel.DAY_CHOICES]
        # Define una grilla fija de horas (ajústala a tu jornada)
        # 07:00, 09:00, 11:00, ...
        time_slots = [time(hour=h) for h in range(7, 19, 2)]

        for parallel in parallels:
            used_slots = set()  # (day, startTime) por parallel
            # Elige 2-4 materias para este paralelo
            subjects_for_parallel = random.sample(subjects, k=min(4, len(subjects)))
            random.shuffle(subjects_for_parallel)

            # Para cada materia intenta asignar un slot único
            for subject in subjects_for_parallel:
                # baraja días y horas para buscar el primer slot libre
                days = day_choices[:]  # copia
                random.shuffle(days)
                slots = time_slots[:]
                random.shuffle(slots)

                created = False
                for d in days:
                    for s in slots:
                        if (d, s) in used_slots:
                            continue
                        # duración 90 minutos por ejemplo
                        end_hour = (datetime.combine(date.today(), s) +
                                    timedelta(minutes=90)).time()
                        # Garantiza no chocar con la unicidad
                        obj, made = ClassScheduleModel.objects.get_or_create(
                            course=parallel.course,
                            parallel=parallel,
                            schoolYear=parallel.schoolYear,
                            subject=subject,
                            dayOfWeek=d,
                            startTime=s,
                            defaults={"endTime": end_hour},
                        )
                        if made:
                            used_slots.add((d, s))
                            created = True
                            break
                    if created:
                        break
                # Si no encontró hueco libre, lo omite (evita IntegrityError)

        # ---------- GRADING SYSTEMS ----------
        grading_systems = []
        for i in range(2):
            gs = GradingSystemModel.objects.create(
                name=f"Sistema de Notas {i+1}",
                description=fake.text(),
                numberOfTerms=3,
                passingScore=7.00
            )
            grading_systems.append(gs)

        # ---------- GRADING TERMS ----------
        for gs in grading_systems:
            for order in range(1, gs.numberOfTerms + 1):
                GradingTermModel.objects.create(
                    gradingSystem=gs,
                    academicYear=random.choice(school_years),
                    name=f"Term {order}",
                    order=order,
                    weight=round(100 / gs.numberOfTerms, 2)
                )

        # ---------- EVALUATION TYPES ----------
        for i in range(3):
            EvaluationTypeModel.objects.create(
                name=f"Evaluación {i+1}",
                description=fake.text(),
                weight=round(random.uniform(10, 40), 2)
            )

        # ---------- CONFIGURATION ----------
        for i in range(3):
            ConfigurationModel.objects.create(
                key=f"config_{i}",
                value=fake.word(),
                description=fake.text()
            )

        # ---------- MEETING TYPES ----------
        for i in range(2):
            MeetingTypeModel.objects.create(
                name=f"Reunión {i+1}",
                description=fake.text()
            )

        # ---------- ATTENDANCE CODES ----------
        for i in range(3):
            AttendanceCodeModel.objects.create(
                code=f"A{i+1}",
                description=fake.text(),
                affectsGrade=random.choice([True, False])
            )

        # ---------- BEHAVIOR SCALES ----------
        for i in range(3):
            BehaviorScaleModel.objects.create(
                name=f"Escala {i+1}",
                minScore=0.00,
                maxScore=10.00
            )

        # ---------- LOG ACTIVITY ----------
        for i in range(10):
            LogActivityModel.objects.create(
                userId=fake.uuid4(),
                action=fake.word(),
                description=fake.text()
            )

        # ---------- ACADEMIC PLANNING ----------
        # ---------- ACADEMIC PLANNING ----------
        for parallel in parallels:
            # crea 1-2 planificaciones por paralelo asegurando unicidad por startDate
            n_plans = random.randint(1, 2)
            start = parallel.schoolYear.startDate
            for i in range(n_plans):
                subj = random.choice(subjects)
                plan_start = start + timedelta(days=i * 30)
                plan_end = plan_start + timedelta(days=20)
                AcademicPlanningModel.objects.get_or_create(
                    course=parallel.course,
                    parallel=parallel,
                    schoolYear=parallel.schoolYear,
                    subject=subj,
                    startDate=plan_start,
                    defaults={
                        "topic": fake.sentence(),
                        "endDate": plan_end,
                        "description": fake.text(),
                    },
                )


        self.stdout.write(self.style.SUCCESS(
            "Datos falsos generados correctamente."))
