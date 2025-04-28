from rest_framework.serializers import Serializer, CharField, IntegerField


class SectionSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    type = CharField(max_length=50)
    description = CharField(max_length=500, allow_blank=True, required=False)

