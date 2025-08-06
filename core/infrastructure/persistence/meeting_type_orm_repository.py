from core.domain.entities.meeting_type import MeetingType
from core.domain.repositories.meeting_type_repository import MeetingTypeRepository
from core.models import MeetingTypeModel
from django.utils import timezone

class MeetingTypeOrmRepository(MeetingTypeRepository):
    def get(self, meeting_type_id: int) -> MeetingType:
        model = MeetingTypeModel.objects.get(id=meeting_type_id, deleted=False)
        return MeetingType(
            id=model.id,
            name=model.name,
            description=model.description,
        )

    def all(self):
        models = MeetingTypeModel.objects.filter(deleted=False).order_by('name')
        return [
            MeetingType(
                id=m.id,
                name=m.name,
                description=m.description,
            )
            for m in models
        ]

    def create(self, meeting_type: MeetingType) -> MeetingType:
        model = MeetingTypeModel(
            name=meeting_type.name,
            description=meeting_type.description,
        )
        model.save()
        meeting_type.id = model.id
        return meeting_type

    def update(self, meeting_type: MeetingType) -> MeetingType:
        model = MeetingTypeModel.objects.get(id=meeting_type.id, deleted=False)
        model.name = meeting_type.name
        model.description = meeting_type.description
        model.save()
        return meeting_type

    def delete(self, meeting_type_id: int) -> bool:
        model = MeetingTypeModel.objects.get(id=meeting_type_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_name(self, name: str) -> bool:
        return MeetingTypeModel.objects.filter(name=name, deleted=False).exists()

    def exist_by_id(self, meeting_type_id: int) -> bool:
        return MeetingTypeModel.objects.filter(id=meeting_type_id, deleted=False).exists()
