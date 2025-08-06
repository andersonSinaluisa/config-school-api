from rest_framework import serializers

class GradingSystemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    numberOfTerms = serializers.IntegerField()
    passingScore = serializers.DecimalField(max_digits=5, decimal_places=2)
