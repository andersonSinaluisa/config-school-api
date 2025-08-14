from core.domain.entities.course import Course
from core.domain.entities.couse_subject import CourseSubject
from core.domain.repositories.course_subject_repository import CourseSubjectRepository
from core.models import CourseSubjectModel
from django.utils import timezone


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
        course_subject.deleted_at = timezone.now()
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
    
    def get_by_course_and_subject(self, course_id, subject_id):
        try:
            course_subject = CourseSubjectModel.objects.get(
                course_id=course_id,
                subject_id=subject_id,
                deleted=False
            )
            return CourseSubject(
                courseId=course_subject.id,
                hoursPerWeek=course_subject.hoursPerWeek,
                id=course_subject.course.id,
                subjectId=course_subject.subject.id,
                isRequired=course_subject.isRequired,
                course=course_subject.course,
                subject=course_subject.subject
            )
        except CourseSubjectModel.DoesNotExist:
            return None

    def get_by_course(self, course_id):
        course_subjects = CourseSubjectModel.objects.filter(
            course_id=course_id, deleted=False).order_by('id')
        return [
            CourseSubject(
                id=course_subject.id,
                hoursPerWeek=course_subject.hoursPerWeek,
                courseId=course_subject.course.id,
                subjectId=course_subject.subject.id,
                isRequired=course_subject.isRequired,
                course=course_subject.course,
                subject=course_subject.subject
            ) for course_subject in course_subjects
        ]
        
        
    def create_range(self, course_subjects):
        course_subject_models = [
            CourseSubjectModel(
                course_id=course_subject.courseId,
                subject_id=course_subject.subjectId,
                hoursPerWeek=course_subject.hoursPerWeek,
                isRequired=course_subject.isRequired
            ) for course_subject in course_subjects
        ]
        CourseSubjectModel.objects.bulk_create(course_subject_models)
        return course_subjects
    
    
    def remove_from_course(self, course_id, subject_id):
        CourseSubjectModel.objects.filter(course_id=course_id, subject_id=subject_id).delete()
        return True
    
    def remove_range_from_course(self, course_subjects_ids):
        CourseSubjectModel.objects.filter(id__in=course_subjects_ids).update(
            deleted=True,
            deleted_at=timezone.now()
        )
        return True