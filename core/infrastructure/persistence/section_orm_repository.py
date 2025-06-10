

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
                break_count= section.break_count,
                break_duration=section.break_duration,
                start_time=section.start_time,
                end_time=section.end_time,
                has_break=section.has_break,
                days=section.days if section.days.split(',') else []
                
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
            break_count=section.breakCount,
            break_duration=section.breakDuration,
            start_time=section.startDate,
            end_time=section.endDate,
            has_break=section.hasBreak,
            days=section.days.split(',') if section.days else []
            
        )

    def create(self, section):
        section_ = SectionModel.objects.create(
            name=section.name,
            type=section.type,
            description=section.description,
            start_time=section.start_time,
            end_time=section.end_time,
            has_break=section.has_break,
            break_count=section.break_count,
            break_duration=section.break_duration,
            days= ','.join(section.days) if section.days else ''
        )

        return Section(
            id=section_.id,
            name=section_.name,
            type=section_.type,
            description=section_.description,
            break_count=section_.breakCount,
            break_duration=section_.breakDuration,
            start_time=section_.startDate,
            end_time=section_.endDate,
            has_break=section_.hasBreak,
            days=section_.days.split(',') if section_.days else []
        )

    def update(self, section):
        section_ = SectionModel.objects.get(id=section.id, deleted=False)

        section_.name = section.name
        section_.type = section.type
        section_.description = section.description
        section_.startDate = section.start_time
        section_.endDate = section.end_time
        section_.hasBreak = section.has_break
        section_.breakCount = section.break_count
        section_.breakDuration = section.break_duration
        section_.days = ','.join(section.days) if section.days else ''
        
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

    