from rest_framework import serializers

from core.application.serializers.course_serializer import CoursePartialSerializer
from core.application.serializers.parallel_serializer import ParallelPartialSerializer
from core.application.serializers.school_year_serializer import SchoolYearSerializer
from core.application.serializers.subject_serializer import SubjectSerializer


class AcademicPlanningSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_id = serializers.IntegerField()
    parallel_id = serializers.IntegerField()
    school_year_id = serializers.IntegerField()
    subject_id = serializers.IntegerField()
    topic = serializers.CharField(max_length=255)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    course = CoursePartialSerializer(read_only=True)
    parallel = ParallelPartialSerializer(read_only=True)
    school_year = SchoolYearSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
