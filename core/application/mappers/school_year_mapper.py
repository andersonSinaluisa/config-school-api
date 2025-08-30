from core.domain.entities.school_year import SchoolYear


def school_year_model_to_entity(school_year_model):
    if not school_year_model:
        return None
    return SchoolYear(
        id=school_year_model.id,
        name=school_year_model.name,
        startDate=school_year_model.startDate,
        endDate=school_year_model.endDate,
        status=school_year_model.status,
    )
