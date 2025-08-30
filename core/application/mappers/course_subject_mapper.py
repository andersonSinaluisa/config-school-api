from core.domain.entities.couse_subject import CourseSubject
from core.domain.entities.subject import Subject
from core.models import CourseSubjectModel


def course_subject_model_to_entity(model: CourseSubjectModel) -> CourseSubject:
    subject_entity = Subject(
        id=model.subject.id,
        name=model.subject.name,
        hoursPerWeek=model.subject.hoursPerWeek,
        code=model.subject.code,
        description=model.subject.description
    )
    return CourseSubject(
        id=model.id,
        courseId=model.course_id,
        subjectId=model.subject_id,
        subject=subject_entity,
        hoursPerWeek=model.subject.hoursPerWeek,
        isRequired=model.isRequired
    )
