

from core.domain.entities.section import Section
from core.domain.repositories.section_repository import SectionRepository
from core.models import SectionModel
from django.utils import timezone

class SectionOrmRepository(SectionRepository):
    def all(self):
        sections = SectionModel.objects.filter(deleted=False).order_by('id')

        return [
            Section(
                id=section.id,
                name=section.name,
                type=section.type,
                description=section.description,
            )
            for section in sections
        ]

    def get(self, section_id):
        section = SectionModel.objects.get(id=section_id, deleted=False)

        return Section(
            id=section.id,
            name=section.name,
            type=section.type,
            description=section.description,
        )

    def create(self, section):
        section_ = SectionModel.objects.create(
            name=section.name,
            type=section.type,
            description=section.description,
        )

        return Section(
            id=section_.id,
            name=section_.name,
            type=section_.type,
            description=section_.description,
        )

    def update(self, section):
        section_ = SectionModel.objects.get(id=section.id, deleted=False)

        section_.name = section.name
        section_.type = section.type
        section_.description = section.description

        section_.save()

        return Section(
            id=section_.id,
            name=section_.name,
            type=section_.type,
            description=section_.description,
        )

    def delete(self, section_id):
        section_ = SectionModel.objects.get(id=section_id, deleted=False)
    
        section_.deleted = True
        section_.deleted_at = timezone.now()
        section_.save()

    def exist_by_id(self, section_id):
        return SectionModel.objects.filter(id=section_id, deleted=False).exists()

    def exist_by_name(self, name):
        return SectionModel.objects.filter(name=name, deleted=False).exists()

    