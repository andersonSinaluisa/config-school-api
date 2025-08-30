from core.domain.entities.course import Course


def course_model_to_entity(course_model):
    if not course_model:
        return None
    return Course(
        id=course_model.id,
        name=course_model.name,
        level_id=course_model.level_id,
        description=course_model.description,
    )
