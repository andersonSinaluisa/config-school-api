from rest_framework import serializers

class BehaviorScaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    minScore = serializers.DecimalField(max_digits=5, decimal_places=2)
    maxScore = serializers.DecimalField(max_digits=5, decimal_places=2)
