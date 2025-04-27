from rest_framework.serializers import Serializer, CharField, IntegerField


class SubjectSerializer(Serializer):

    
    id = IntegerField(read_only=True)
    name = CharField(max_length=100, required=True)
    code = CharField(max_length=10, required=True)
    description = CharField(max_length=255, required=True)
    hoursPerWeek = IntegerField(required=True)
