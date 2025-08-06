from core.domain.repositories.meeting_type_repository import MeetingTypeRepository
from rest_framework.exceptions import NotFound, ValidationError
import logging

class ListMeetingTypeService:
    def __init__(self, meeting_type_repository: MeetingTypeRepository):
        self.meeting_type_repository = meeting_type_repository

    def execute(self):
        try:
            return self.meeting_type_repository.all()
        except Exception as e:
            logging.error(f"Error listing meeting types: {e}")
            if isinstance(e, NotFound):
                raise NotFound("No meeting types found")
            elif isinstance(e, ValidationError):
                raise ValidationError("Invalid meeting type data")
            else:
                raise Exception("An unexpected error occurred") from e
