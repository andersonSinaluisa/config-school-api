from rest_framework import serializers

class MeetingTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True, required=False)
