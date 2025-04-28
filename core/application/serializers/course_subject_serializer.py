from rest_framework.serializers import Serializer,CharField, IntegerField, BooleanField


class CourseSubjectSerializer(Serializer):
    id = IntegerField(read_only=True)
    courseId = IntegerField(required=True)
    subjectId = IntegerField(required=True)
    hoursPerWeek = IntegerField(required=True)
    isRequired = BooleanField(required=True)