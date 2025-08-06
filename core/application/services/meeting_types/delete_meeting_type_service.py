from core.domain.repositories.meeting_type_repository import MeetingTypeRepository
from rest_framework.exceptions import NotFound

class DeleteMeetingTypeService:
    def __init__(self, meeting_type_repository: MeetingTypeRepository):
        self.meeting_type_repository = meeting_type_repository

    def execute(self, meeting_type_id: int):
        if not self.meeting_type_repository.exist_by_id(meeting_type_id):
            raise NotFound("Meeting type not found")
        return self.meeting_type_repository.delete(meeting_type_id)
