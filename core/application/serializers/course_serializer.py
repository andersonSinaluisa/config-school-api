from rest_framework import serializers

from core.application.serializers.level_serializer import LevelSerializer

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    level_id = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    level = LevelSerializer(read_only=True)
    
    def validate(self, data):
        # Custom validation logic can be added here if needed
        if 'name' in data and len(data['name']) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        if 'description' in data and len(data['description']) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        if 'level_id' in data and data['level_id'] <= 0:
            raise serializers.ValidationError("Level ID must be a positive integer.")

        return data

class CoursePartialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=False)
    level_id = serializers.IntegerField(required=False)
    description = serializers.CharField(max_length=255, required=False)
    level = LevelSerializer(read_only=True)
