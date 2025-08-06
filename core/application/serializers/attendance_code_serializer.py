from rest_framework import serializers

class AttendanceCodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=255)
    affectsGrade = serializers.BooleanField(default=False)
