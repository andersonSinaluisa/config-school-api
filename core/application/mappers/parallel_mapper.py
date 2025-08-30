from core.domain.entities.parallel import Parallel
from core.application.mappers.course_mapper import course_model_to_entity
from core.application.mappers.section_mapper import section_model_to_entity
from core.application.mappers.school_year_mapper import school_year_model_to_entity


def parallel_model_to_entity(parallel_model):
    if not parallel_model:
        return None
    return Parallel(
        id=parallel_model.id,
        name=parallel_model.name,
        course_id=parallel_model.course.id,
        capacity=parallel_model.capacity,
        section_id=parallel_model.section.id,
        school_year_id=parallel_model.schoolYear.id,
        course=course_model_to_entity(parallel_model.course),
        section=section_model_to_entity(parallel_model.section),
        school_year=school_year_model_to_entity(parallel_model.schoolYear),
    )
