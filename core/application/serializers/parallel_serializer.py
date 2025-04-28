from rest_framework import serializers

class ParallelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    course_id = serializers.IntegerField()
    capacity = serializers.IntegerField()
    section_id = serializers.IntegerField()
    school_year_id = serializers.IntegerField()
