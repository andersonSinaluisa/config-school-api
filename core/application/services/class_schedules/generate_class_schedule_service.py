from datetime import datetime, timedelta
from ortools.sat.python import cp_model
from core.domain.entities.class_schedule import ClassSchedule
from rest_framework.exceptions import ValidationError


class GenerateClassScheduleService:

    def __init__(self, parallel_repository,
                 course_subject_repository,
                 section_break_repository,
                 class_schedule_repository,
                 ):
        self.parallel_repository = parallel_repository
        self.course_subject_repository = course_subject_repository
        self.section_break_repository = section_break_repository
        self.class_schedule_repository = class_schedule_repository

    def overlaps(self, start1, end1, start2, end2):
        """Verifica si dos rangos de tiempo se cruzan."""
        return start1 < end2 and start2 < end1

    def normalize_to_slot(self, time_value, slots, slot_duration):
        """Encuentra el índice del slot al que pertenece un start_time."""
        t_dt = datetime.combine(datetime.today(), time_value)
        for idx, s in enumerate(slots):
            s_dt = datetime.combine(datetime.today(), s)
            e_dt = s_dt + slot_duration
            if s_dt <= t_dt < e_dt:
                return idx
        return None

    def execute(self, parallel_id):

        parallel = self.parallel_repository.get(parallel_id)
        if not parallel:
            raise ValueError("Parallel not found")

        course = parallel.course
        section = parallel.section
        school_year = parallel.school_year

        # Días configurados en la sección
        days = section.days.split(",") if section.days else []

        # Slots de clase (bloques horarios)
        start_time = section.start_time
        end_time = section.end_time
        slot_duration = timedelta(
            hours=section.class_duration.hour,
            minutes=section.class_duration.minute,
            seconds=section.class_duration.second
        )

        slots = []
        current = datetime.combine(datetime.today(), start_time)
        while current.time() < end_time:
            slots.append(current.time())
            current += slot_duration

        # Materias del curso
        course_subjects = self.course_subject_repository.get_by_course(
            course.id)

        # Breaks configurados para la sección
        section_breaks = self.section_break_repository.all(
            section_id=section.id)

        # Organizar breaks por día
        breaks_by_day = {day: [] for day in days}
        for br in section_breaks:
            breaks_by_day[br.day].append((br.start_time, br.end_time))

        # Identificar slots prohibidos por superposición con breaks
        forbidden_slots = set()
        for d, day in enumerate(days):
            for s, slot in enumerate(slots):
                slot_end = (datetime.combine(
                    datetime.today(), slot) + slot_duration).time()
                for br_start, br_end in breaks_by_day.get(day, []):
                    if slot < br_end and slot_end > br_start:  # hay cruce
                        forbidden_slots.add((d, s))

        # ✅ Obtener los ya asignados
        assigned_schedules = self.class_schedule_repository.filter_by_parallel_and_subject(
            parallel_id=parallel_id,
            subject_id=None
        )

        assigned_map = {}
        for sc in assigned_schedules:
            try:
                d = days.index(sc.day_of_week)   # en tu modelo: dayOfWeek
                s = self.normalize_to_slot(sc.start_time, slots, slot_duration)
                if s is not None:
                    assigned_map[(d, s)] = sc.subject_id
            except ValueError:
                continue

        # Modelo CP-SAT
        model = cp_model.CpModel()

        # Variables de decisión
        X = {}
        for i, cs in enumerate(course_subjects):
            for d, day in enumerate(days):
                for s, slot in enumerate(slots):
                    X[(i, d, s)] = model.NewBoolVar(f"x_{i}_{day}_{slot}")

        # Duración del bloque en horas
        slot_duration_hours = (
            section.class_duration.hour +
            section.class_duration.minute / 60 +
            section.class_duration.second / 3600
        )

        # Restricción: cada materia no puede exceder sus horas semanales (en slots)
        for i, cs in enumerate(course_subjects):
            h, m, s = cs.hoursPerWeek.hour, cs.hoursPerWeek.minute, cs.hoursPerWeek.second


            subject_hours = h + m/60 + s/3600  # float en horas
            max_slots = int(round(subject_hours / slot_duration_hours))

            fixed_count = sum(1 for (d, s), subj in assigned_map.items()
                              if subj == cs.subject.id)

            total_new = sum(
                X[(i, d, s)]
                for d in range(len(days))
                for s in range(len(slots))
                if (d, s) not in assigned_map
            )

            if fixed_count > max_slots:
                raise ValueError(
                    f"La materia {cs.subject.name} ya excede sus horas: "
                    f"{fixed_count} slots asignados vs {max_slots} permitidos"
                )

            model.Add(fixed_count + total_new == max_slots)

        # Restricción: no dos materias en el mismo slot
        for d in range(len(days)):
            for s in range(len(slots)):
                model.Add(
                    sum(X[(i, d, s)] for i in range(len(course_subjects))) <= 1
                )

        # Restricción: prohibir slots en horarios de break
        for (d, s) in forbidden_slots:
            for i in range(len(course_subjects)):
                model.Add(X[(i, d, s)] == 0)

        # Slots ya asignados → fijarlos
        for (d, s), subj_id in assigned_map.items():
            for i, cs in enumerate(course_subjects):
                if cs.subject.id == subj_id:
                    model.Add(X[(i, d, s)] == 1)
                else:
                    model.Add(X[(i, d, s)] == 0)

        # Balancear carga entre días
        day_loads = []
        for d in range(len(days)):
            load = sum(
                X[(i, d, s)]
                for i in range(len(course_subjects))
                for s in range(len(slots))
            )
            day_loads.append(load)

        max_slots_total = len(days) * len(slots)
        max_load = model.NewIntVar(0, max_slots_total, "max_load")
        min_load = model.NewIntVar(0, max_slots_total, "min_load")
        model.AddMaxEquality(max_load, day_loads)
        model.AddMinEquality(min_load, day_loads)
        model.Minimize(max_load - min_load)

        # Resolver
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 10
        status = solver.Solve(model)

        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            raise ValidationError("No se pudo encontrar un horario válido")

        # Construir horarios resultantes
        schedules = []
        schedules.extend(assigned_schedules)  # primero los ya asignados

        existing = {(s.day_of_week, s.start_time, s.end_time)
                    for s in assigned_schedules}

        # luego los nuevos sugeridos
        for i, cs in enumerate(course_subjects):
            for d, day in enumerate(days):
                for s, slot in enumerate(slots):
                    if solver.Value(X[(i, d, s)]) == 1:
                        start = slot
                        end = (datetime.combine(datetime.today(),
                               slot) + slot_duration).time()

                        if any(
                            existing_day == day and self.overlaps(
                                start, end, ex_start, ex_end)
                            for (existing_day, ex_start, ex_end) in existing
                        ):
                            continue

                        schedule = ClassSchedule(
                            id=0,
                            course_id=course.id,
                            parallel_id=parallel.id,
                            school_year_id=school_year.id,
                            subject_id=cs.subject.id,
                            day_of_week=day,
                            start_time=start,
                            end_time=end,
                            subject=cs.subject,
                            course=course,
                            school_year=school_year,
                        )
                        schedules.append(schedule)

        return schedules
