from rest_framework import serializers


class SectionBreakSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    section_id = serializers.IntegerField()
    day = serializers.CharField(max_length=10)
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

