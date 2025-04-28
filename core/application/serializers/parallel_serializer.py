from rest_framework import serializers

from core.application.serializers.course_serializer import CourseSerializer
from core.application.serializers.section_serializer import SectionSerializer

class ParallelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    course_id = serializers.IntegerField()
    capacity = serializers.IntegerField()
    section_id = serializers.IntegerField()
    school_year_id = serializers.IntegerField()
    course = CourseSerializer(read_only=True)
    section = SectionSerializer(read_only=True)