
from core.domain.repositories.parallel_repository import ParallelRepository
from core.domain.repositories.course_subject_repository import CourseSubjectRepository

from datetime import datetime, timedelta
from ortools.sat.python import cp_model
from core.domain.entities.class_schedule import ClassSchedule


class GenerateClassScheduleService:

    def __init__(self, parallel_repository:ParallelRepository,
                 course_subject_repository: CourseSubjectRepository
                 ):
        self.parallel_repository = parallel_repository
        self.course_subject_repository = course_subject_repository

    def execute(self, parallel_id):
        
        parallel = self.parallel_repository.get(parallel_id)
        if not parallel:
            raise ValueError("Parallel not found")
        course = parallel.course
        section = parallel.section
        school_year = parallel.school_year
        
        days = section.days.split(",") if section.days else []

        start_time = section.start_time
        end_time = section.end_time
        slot_duration = timedelta(hours=section.class_duration.hour,
                  minutes=section.class_duration.minute, seconds=section.class_duration.second)

        slots = []
        current = datetime.combine(datetime.today(), start_time)
        while current.time() < end_time:
            slots.append(current.time())
            current += slot_duration
            
        course_subjects = self.course_subject_repository.get_by_course(
            course.id)

        model = cp_model.CpModel()
        total_slots = len(days) * len(slots)


        total_hours_needed = sum(cs.subject.hoursPerWeek for cs in course_subjects)
        print("Slots disponibles:", total_slots)
        print("Horas requeridas:", total_hours_needed)
        for cs in course_subjects:
            print(cs.subject.name, cs.subject.hoursPerWeek)
    
        X = {}
        for i, cs in enumerate(course_subjects):
            for d, day in enumerate(days):
                for s, slot in enumerate(slots):
                    X[(i, d, s)] = model.NewBoolVar(f"x_{i}_{day}_{slot}")

        # Restricción: cada materia debe cumplir con sus horas semanales
        for i, cs in enumerate(course_subjects):
            subject_hours = cs.subject.hoursPerWeek
            model.Add(sum(X[(i, d, s)] for d in range(len(days))
                      for s in range(len(slots))) == subject_hours)
            
         # Restricción: un paralelo no puede tener dos materias en el mismo slot
        for d in range(len(days)):
            for s in range(len(slots)):
                model.Add(sum(X[(i, d, s)]
                          for i in range(len(course_subjects))) <= 1)
                
        day_loads = []
        for d in range(len(days)):
            load = sum(X[(i, d, s)] for i in range(len(course_subjects))
                       for s in range(len(slots)))
            day_loads.append(load)


        # Objetivo: minimizar diferencia entre el día más cargado y el menos cargado
        max_load = model.NewIntVar(0, 40, "max_load")
        min_load = model.NewIntVar(0, 40, "min_load")

        model.AddMaxEquality(max_load, day_loads)
        model.AddMinEquality(min_load, day_loads)

        # Minimizar el rango de carga
        model.Minimize(max_load - min_load)

        # Resolver
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 10  # límite de tiempo
        status = solver.Solve(model)

        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            raise ValueError("No se pudo encontrar un horario válido")

        schedules = []
        for i, cs in enumerate(course_subjects):
            for d, day in enumerate(days):
                for s, slot in enumerate(slots):
                    if solver.Value(X[(i, d, s)]) == 1:
                        schedule = ClassSchedule(
                            id=0,
                            course_id=course.id,
                            parallel_id=parallel.id,
                            school_year_id=school_year.id,
                            subject_id=cs.subjectId,
                            day_of_week=day,
                            start_time=slot,
                            end_time=(datetime.combine(datetime.today(), slot) + slot_duration).time(),
                            subject=cs.subject,
                            course=course,
                            school_year=school_year,
                        )

                        schedules.append(schedule)
        return schedules
