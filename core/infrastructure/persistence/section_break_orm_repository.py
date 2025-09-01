from core.domain.entities.section_break import SectionBreak
from core.domain.repositories.section_break_repository import SectionBreakRepository
from core.models import SectionBreakModel
from django.utils import timezone


class SectionBreakOrmRepository(SectionBreakRepository):
    def all(self, *, section_id: int | None = None):
        qs = SectionBreakModel.objects.filter(deleted=False)
        if section_id is not None:
            qs = qs.filter(section_id=section_id)
        qs = qs.order_by('day', 'start_time')
        return [
            SectionBreak(
                id=b.id,
                section_id=b.section_id,
                day=b.day,
                start_time=b.start_time,
                end_time=b.end_time,
            )
            for b in qs
        ]

    def get(self, section_break_id: int):
        b = SectionBreakModel.objects.get(id=section_break_id, deleted=False)
        return SectionBreak(
            id=b.id,
            section_id=b.section_id,
            day=b.day,
            start_time=b.start_time,
            end_time=b.end_time,
        )

    def create(self, section_break: SectionBreak) -> SectionBreak:
        model = SectionBreakModel.objects.create(
            section_id=section_break.section_id,
            day=section_break.day,
            start_time=section_break.start_time,
            end_time=section_break.end_time,
        )
        return SectionBreak(
            id=model.id,
            section_id=model.section_id,
            day=model.day,
            start_time=model.start_time,
            end_time=model.end_time,
        )

    def update(self, section_break: SectionBreak) -> SectionBreak:
        model = SectionBreakModel.objects.get(id=section_break.id, deleted=False)
        model.section_id = section_break.section_id
        model.day = section_break.day
        model.start_time = section_break.start_time
        model.end_time = section_break.end_time
        model.save()
        return SectionBreak(
            id=model.id,
            section_id=model.section_id,
            day=model.day,
            start_time=model.start_time,
            end_time=model.end_time,
        )

    def delete(self, section_break_id: int) -> bool:
        model = SectionBreakModel.objects.get(id=section_break_id, deleted=False)
        model.deleted = True
        model.deleted_at = timezone.now()
        model.save()
        return True

    def exist_by_id(self, section_break_id: int) -> bool:
        return SectionBreakModel.objects.filter(id=section_break_id, deleted=False).exists()

    def exist_by_section_day_time(self, section_id: int, day: str, start_time) -> bool:
        return SectionBreakModel.objects.filter(
            section_id=section_id,
            day=day,
            start_time=start_time,
            deleted=False,
        ).exists()

