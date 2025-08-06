from core.domain.entities.meeting_type import MeetingType
from core.domain.repositories.meeting_type_repository import MeetingTypeRepository
from rest_framework.exceptions import ValidationError

class CreateMeetingTypeService:
    def __init__(self, meeting_type_repository: MeetingTypeRepository):
        self.meeting_type_repository = meeting_type_repository

    def execute(self, name, description):
        if self.meeting_type_repository.exist_by_name(name):
            raise ValidationError("Meeting type with this name already exists.")
        meeting_type = MeetingType(
            id=None,
            name=name,
            description=description,
        )
        return self.meeting_type_repository.create(meeting_type)
