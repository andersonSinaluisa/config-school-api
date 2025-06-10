
from typing import List
from core.domain.entities.couse_subject import CourseSubject
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from rest_framework.exceptions import ValidationError
class CreateRangeCourseSubjectService:
    def __init__(self, course_subject_repository: CourseSubjectRepository):
        self.course_subject_repository = course_subject_repository

    def execute(self, course_id: int, course_subjects: List[dict]) -> List[CourseSubject]:
        """
        Create or update a range of CourseSubject entities for a course.
        Removes any CourseSubjects that are no longer present.
        """
        if not course_subjects:
            raise ValueError("Course subjects list cannot be empty")

        # Convertir los dicts en objetos CourseSubject
        incoming_subjects = [
            CourseSubject(
                id=None,  # Será actualizado si ya existe
                courseId=course_id,
                subjectId=cs['subjectId'],
                hoursPerWeek=cs['hoursPerWeek'],
                isRequired=cs['isRequired']
            ) for cs in course_subjects
        ]

        # Obtener los actuales del repositorio
        existing_subjects = self.course_subject_repository.get_by_course(
            course_id)

        # Índices por subjectId para comparaciones rápidas
        existing_map = {(cs.subjectId, cs.courseId)
                         : cs for cs in existing_subjects}
        incoming_map = {(cs.subjectId, cs.courseId)
                         : cs for cs in incoming_subjects}

        # Determinar cuáles actualizar, crear o eliminar
        to_update = []
        to_create = []
        to_delete = []

        for key, incoming_cs in incoming_map.items():
            if key in existing_map:
                existing_cs = existing_map[key]
                incoming_cs.id = existing_cs.id  # Mantener ID existente
                to_update.append(incoming_cs)
            else:
                to_create.append(incoming_cs)

        for key, existing_cs in existing_map.items():
            if key not in incoming_map:
                to_delete.append(existing_cs)

        # Persistir los cambios
        for cs in to_update:
            self.course_subject_repository.update(cs)
        for cs in to_delete:
            self.course_subject_repository.remove_from_course(
                course_id, cs.subjectId)
        created = self.course_subject_repository.create_range(to_create)

        # Retornar todos los CourseSubjects activos tras la operación
        return to_update + created
