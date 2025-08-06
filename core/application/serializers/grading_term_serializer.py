from rest_framework import serializers

class GradingTermSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gradingSystem_id = serializers.IntegerField()
    academicYear_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    order = serializers.IntegerField()
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
