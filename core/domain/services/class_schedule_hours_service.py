from datetime import datetime, date, timedelta, time
from rest_framework.exceptions import ValidationError
from core.domain.entities.class_schedule import ClassSchedule


class ClassScheduleHoursService:
    @staticmethod
    def calculate_duration(start_time, end_time) -> float:
        """
        Calcula la duración en horas entre dos objetos datetime.time.
        Soporta rangos que cruzan medianoche (ej. 22:00 → 01:00).
        """
        start_dt = datetime.combine(date.today(), start_time)
        end_dt = datetime.combine(date.today(), end_time)

        if end_dt < start_dt:
            end_dt += timedelta(days=1)

        return (end_dt - start_dt).total_seconds() / 3600

    @staticmethod
    def calculate_total_hours(new_start, new_end, schedules: list[ClassSchedule]) -> float:
        """
        Calcula el total de horas acumuladas (horarios ya creados + nuevo horario).
        """
        actual_time = sum(
            ClassScheduleHoursService.calculate_duration(
                s.start_time, s.end_time
            )
            for s in schedules
        )

        new_time = ClassScheduleHoursService.calculate_duration(
            new_start, new_end)
        return actual_time + new_time

    @staticmethod
    def time_to_hours(t: time) -> float:
        """
        Convierte un datetime.time a cantidad de horas (float).
        Ejemplo: 04:30 -> 4.5
        """
        return t.hour + t.minute / 60.0

    @staticmethod
    def validate_total_hours(new_start, new_end, schedules, hours_per_week: time):
        """
        Valida que la suma de las horas (existentes + nuevas) no exceda
        las horas asignadas por semana (almacenadas como time).
        """
        total_assigned = ClassScheduleHoursService.calculate_total_hours(
            new_start, new_end, schedules
        )

        max_hours = ClassScheduleHoursService.time_to_hours(hours_per_week)

        if total_assigned > max_hours:
            raise ValidationError(
                f"El total de horas excede las horas asignadas por semana, {max_hours} horas., asignadas {total_assigned}",
                code="exceeds_hours_per_week"
            )
