from core.domain.entities.meeting_type import MeetingType
from core.domain.repositories.meeting_type_repository import MeetingTypeRepository
from rest_framework.exceptions import NotFound

class UpdateMeetingTypeService:
    def __init__(self, meeting_type_repository: MeetingTypeRepository):
        self.meeting_type_repository = meeting_type_repository

    def execute(self, meeting_type_id: int, name, description):
        if not self.meeting_type_repository.exist_by_id(meeting_type_id):
            raise NotFound("Meeting type not found")
        meeting_type = MeetingType(
            id=meeting_type_id,
            name=name,
            description=description,
        )
        return self.meeting_type_repository.update(meeting_type)
