from django.core.management.base import BaseCommand
from django.db import connection
from core import models as m


class Command(BaseCommand):
    help = "Elimina todos los registros de los modelos académicos"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Borrando todos los datos..."))

        # Lista de modelos en orden para evitar errores por FK
        model_order = [
            m.AcademicPlanningModel,
            m.ClassScheduleModel,
            m.CourseSubjectModel,
            m.ParallelModel,
            m.CourseModel,
            m.LevelModel,
            m.SubjectModel,
            m.SectionModel,
            m.SchoolYearModel,
            m.GradingTermModel,
            m.GradingSystemModel,
            m.EvaluationTypeModel,
            m.MeetingTypeModel,
            m.AttendanceCodeModel,
            m.BehaviorScaleModel,
            m.ConfigurationModel,
            m.LogActivityModel,
        ]

        # Borrar en orden
        for model in model_order:
            deleted_count, _ = model.objects.all().delete()
            self.stdout.write(
                f" - {model.__name__}: {deleted_count} registros eliminados")

        # Opcional: resetear secuencias de IDs (PostgreSQL)
        with connection.cursor() as cursor:
            cursor.execute("""
                DO $$ DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
                    LOOP
                        EXECUTE 'ALTER SEQUENCE ' || r.tablename || '_id_seq RESTART WITH 1';
                    END LOOP;
                END $$;
            """)

        self.stdout.write(self.style.SUCCESS(
            "Datos eliminados correctamente."))
