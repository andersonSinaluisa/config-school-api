


from core.domain.entities.school_year import SchoolYear
from core.domain.repositories.school_year_repository import SchoolYearRepository
from core.models import SchoolYearModel
from django.utils import timezone

class SchoolYearOrmRepository(SchoolYearRepository):
    def all(self):
        raise NotImplementedError

    def get(self, school_year_id):
        school_year_ = SchoolYearModel.objects.get(school_year_id,deleted=False)

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.start_date,
            endDate=school_year_.end_date,
            status=school_year_.status,
        )
    def create(self, school_year):
        school_year_ = SchoolYearModel.objects.create(
            name=school_year.name,
            start_date=school_year.startDate,
            end_date=school_year.endDate,
            status=school_year.status,
        )

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.startDate,
            endDate=school_year_.endDate,
            status=school_year_.status,
        )

    def update(self, school_year):
        school_year_ = SchoolYearModel.objects.get(id=school_year.id, deleted=False)

        school_year_.name = school_year.name
        school_year_.startDate = school_year.startDate
        school_year_.endDate = school_year.endDate
        school_year_.status = school_year.status

        school_year_.save()

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.startDate,
            endDate=school_year_.endDate,
            status=school_year_.status,
        )

    def delete(self, school_year_id):
        school_year_ = SchoolYearModel.objects.get(id=school_year_id, deleted=False)

        school_year_.deleted = True
        school_year_.deleted_at = timezone.now()
        school_year_.save()

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.startDate,
            endDate=school_year_.endDate,
            status=school_year_.status,
        )

    def find_by_name(self, name):
        school_year_ = SchoolYearModel.objects.filter(name=name, deleted=False).first()

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.startDate,
            endDate=school_year_.endDate,
            status=school_year_.status,
        )

    def find_by_date_range(self, start_date, end_date):
        school_year_ = SchoolYearModel.objects.filter(
            start_date__gte=start_date,
            end_date__lte=end_date,
            deleted=False
        ).first()

        return SchoolYear(
            id=school_year_.id,
            name=school_year_.name,
            startDate=school_year_.startDate,
            endDate=school_year_.endDate,
            status=school_year_.status,
        )

    def exist_by_id(self, school_year_id):
        return SchoolYearModel.objects.filter(id=school_year_id, deleted=False).exists()

    def exist_by_name(self, name):
        return SchoolYearModel.objects.filter(name=name, deleted=False).exists()
