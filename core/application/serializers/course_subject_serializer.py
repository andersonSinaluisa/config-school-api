from rest_framework.serializers import Serializer,CharField, IntegerField, BooleanField


class CourseSubjectSerializer(Serializer):
    id = IntegerField(read_only=True)
    course_id = IntegerField(required=True)
    subject_id = IntegerField(required=True)
    hours_per_week = IntegerField(required=True)
    is_required = BooleanField(required=True)