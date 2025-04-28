from rest_framework.serializers import Serializer, CharField, IntegerField, DateField


class SchoolYearSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    startDate = DateField()
    endDate = DateField()
    status = CharField(max_length=255, required=False)