from rest_framework.serializers import Serializer, CharField, IntegerField,\
    BooleanField, ListField


class SectionSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    type = CharField(max_length=50)
    description = CharField(max_length=500, allow_blank=True, required=False)
    start_time = CharField(max_length=5)  # HH:MM format
    end_time = CharField(max_length=5)    # HH:MM format
    has_break = BooleanField()
    break_count = IntegerField(min_value=0)
    break_duration = CharField(max_length=5)  # HH:MM format
    days = CharField(max_length=10)

class SectionPartialSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    type = CharField(max_length=50)
    description = CharField(max_length=500, allow_blank=True, required=False)
