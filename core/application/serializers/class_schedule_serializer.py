from rest_framework import serializers

from core.application.serializers.course_serializer import CourseSerializer
from core.application.serializers.parallel_serializer import ParallelSerializer
from core.application.serializers.school_year_serializer import SchoolYearSerializer
from core.application.serializers.subject_serializer import SubjectSerializer


class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_id = serializers.IntegerField()
    parallel_id = serializers.IntegerField()
    school_year_id = serializers.IntegerField()
    subject_id = serializers.IntegerField()
    day_of_week = serializers.CharField(max_length=9)
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    course = CourseSerializer(read_only=True)
    parallel = ParallelSerializer(read_only=True)
    school_year = SchoolYearSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

