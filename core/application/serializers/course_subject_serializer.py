from rest_framework.serializers import Serializer,CharField, IntegerField, BooleanField, TimeField

from core.application.serializers.course_serializer import CourseSerializer
from core.application.serializers.subject_serializer import SubjectSerializer


class CourseSubjectSerializer(Serializer):
    id = IntegerField(read_only=True)
    subjectId = IntegerField(required=True)
    hoursPerWeek = TimeField(required=True)
    isRequired = BooleanField(required=True)
    course = CourseSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
