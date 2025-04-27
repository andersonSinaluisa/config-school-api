


from core.domain.entities.parallel import Parallel
from core.domain.repositories.parallel_repository import ParallelRepository
from core.models import ParallelModel
from django.utils import timezone

class ParallelORMRepository(ParallelRepository):
    def all(self):
        """Get all parallels."""
        parallels = ParallelModel.objects.filter(deleted=False)
        return [Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course_id,
            capacity=parallel.capacity,
            section_id=parallel.section_id,
            school_year_id=parallel.school_year_id
        ) for parallel in parallels]

    def get(self, parallel_id):
        parallel = ParallelModel.objects.get(id=parallel_id, deleted=False)
        return Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course_id,
            capacity=parallel.capacity,
            section_id=parallel.section_id,
            school_year_id=parallel.school_year_id
        )

    def create(self, parallel):
        """Create a new parallel."""
        parallel_model = ParallelModel.objects.create(
            name=parallel.name,
            course_id=parallel.course_id,
            capacity=parallel.capacity,
            section_id=parallel.section_id,
            school_year_id=parallel.school_year_id
        )
        return Parallel(
            id=parallel_model.id,
            name=parallel_model.name,
            course_id=parallel_model.course_id,
            capacity=parallel_model.capacity,
            section_id=parallel_model.section_id,
            school_year_id=parallel_model.school_year_id
        )

    def update(self, parallel):
        """Update an existing parallel."""
        parallel_model = ParallelModel.objects.get(id=parallel.id, deleted=False)
        parallel_model.name = parallel.name
        parallel_model.course_id = parallel.course_id
        parallel_model.capacity = parallel.capacity
        parallel_model.section_id = parallel.section_id
        parallel_model.school_year_id = parallel.school_year_id
        parallel_model.save()
        return Parallel(
            id=parallel_model.id,
            name=parallel_model.name,
            course_id=parallel_model.course_id,
            capacity=parallel_model.capacity,
            section_id=parallel_model.section_id,
            school_year_id=parallel_model.school_year_id
        )
        

    def delete(self, parallel_id):
        """Delete a parallel by its ID."""
        parallel_model = ParallelModel.objects.get(id=parallel_id)
        parallel_model.deleted = True
        parallel_model.deleted_at = timezone.now()
        parallel_model.save()
        return True
    def find_by_id(self, parallel_id):
        """Find a parallel by its ID."""
        parallel = ParallelModel.objects.get(id=parallel_id, deleted=False)
        return Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course_id,
            capacity=parallel.capacity,
            section_id=parallel.section_id,
            school_year_id=parallel.school_year_id
        )

    def exists_by_name(self, name):
        """Check if a parallel exists by its name."""
        return ParallelModel.objects.filter(name=name, deleted=False).exists()

    
    