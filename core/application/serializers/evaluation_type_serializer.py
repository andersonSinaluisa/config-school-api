from rest_framework import serializers

class EvaluationTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
