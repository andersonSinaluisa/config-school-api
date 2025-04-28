from core.domain.entities.course import Course
from core.domain.entities.couse_subject import CourseSubject
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from core.models import CourseSubjectModel


class CourseSubjectOrmRepository(CourseSubjectRepository):
    def get(self, course_id: str):
        course_subject = CourseSubjectModel.objects.get(
            id=course_id, deleted=False)
        return CourseSubject(
            courseId=course_subject.id,
            hoursPerWeek=course_subject.hoursPerWeek,
            id=course_subject.course.id,
            subjectId=course_subject.subject.id,
            isRequired=course_subject.isRequired,
            course=course_subject.course,

        )

    def all(self):
        course_subjects = CourseSubjectModel.objects.filter(
            deleted=False).order_by('id')
        return [
            CourseSubject(
                id=course_subject.id,
                hoursPerWeek=course_subject.hoursPerWeek,
                courseId=course_subject.course.id,
                subjectId=course_subject.subject.id,
                isRequired=course_subject.isRequired,
                course=course_subject.course,

            ) for course_subject in course_subjects
        ]

    def create(self, course: CourseSubject) -> CourseSubject:
        course_subject = CourseSubjectModel.objects.create(
            course_id=course.courseId,
            subject_id=course.subjectId,
            hoursPerWeek=course.hoursPerWeek,
            isRequired=course.isRequired
        )
        return CourseSubject(
            courseId=course_subject.id,
            hoursPerWeek=course_subject.hoursPerWeek,
            id=course_subject.course.id,
            subjectId=course_subject.subject.id,
            isRequired=course_subject.isRequired
        )

    def update(self, course: CourseSubject) -> CourseSubject:
        course_subject = CourseSubjectModel.objects.get(
            id=course.id, deleted=False)
        course_subject.hoursPerWeek = course.hoursPerWeek
        course_subject.subject_id = course.subjectId
        course_subject.isRequired = course.isRequired
        course_subject.save()
        return CourseSubject(
            courseId=course_subject.id,
            hoursPerWeek=course_subject.hoursPerWeek,
            id=course_subject.course.id,
            subjectId=course_subject.subject.id,
            isRequired=course_subject.isRequired
        )

    def delete(self, course_id: str):
        course_subject = CourseSubjectModel.objects.get(id=course_id, deleted=False)
        course_subject.deleted = True
        course_subject.save()
        return CourseSubject(
            courseId=course_subject.id,
            hoursPerWeek=course_subject.hoursPerWeek,
            id=course_subject.course.id,
            subjectId=course_subject.subject.id,
            isRequired=course_subject.isRequired
        )

    def exist_by_course_and_subject(self, course_id, subject_id):
        return CourseSubjectModel.objects.filter(
            course_id=course_id,
            subject_id=subject_id,
            deleted=False
        ).exists()