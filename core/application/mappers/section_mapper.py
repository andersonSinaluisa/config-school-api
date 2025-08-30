from core.domain.entities.section import Section


def section_model_to_entity(section_model):
    if not section_model:
        return None
    return Section(
        id=section_model.id,
        name=section_model.name,
        type=section_model.type,
        description=section_model.description,
        start_time=section_model.startDate,
        end_time=section_model.endDate,
        has_break=section_model.hasBreak,
        break_count=section_model.breakCount,
        break_duration=section_model.breakDuration,
        days=section_model.days,
        class_duration=section_model.class_duration
    )
