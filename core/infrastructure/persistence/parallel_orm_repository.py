


from core.domain.entities.parallel import Parallel
from core.domain.repositories.parallel_repository import ParallelRepository
from core.models import ParallelModel
from django.utils import timezone

from core.application.mappers.course_mapper import course_model_to_entity
from core.application.mappers.section_mapper import section_model_to_entity
from core.application.mappers.school_year_mapper import school_year_model_to_entity

class ParallelORMRepository(ParallelRepository):
    def all(self):
        """Get all parallels."""
        parallels = ParallelModel.objects.filter(deleted=False).order_by('id')
        return [Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course.id,
            capacity=parallel.capacity,
            section_id=parallel.section.id,
            school_year_id=parallel.schoolYear.id,
            course=parallel.course,
            section=parallel.section,
            school_year = parallel.schoolYear

        ) for parallel in parallels]

    def get(self, parallel_id):
        parallel = ParallelModel.objects.get(id=parallel_id, deleted=False)
        return Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course.id,
            capacity=parallel.capacity,
            section_id=parallel.section.id,
            school_year_id=parallel.schoolYear.id,
            course=course_model_to_entity(parallel.course),

            section=section_model_to_entity(parallel.section),
               
            school_year= school_year_model_to_entity(parallel.schoolYear)
        )
        
    

    def create(self, parallel):
        """Create a new parallel."""
        parallel_model = ParallelModel.objects.create(
            name=parallel.name,
            course_id=parallel.course_id,
            capacity=parallel.capacity,
            section_id=parallel.section_id,
            schoolYear_id=parallel.school_year_id
        )
        return Parallel(
            id=parallel_model.id,
            name=parallel_model.name,
            course_id=parallel_model.course.id,
            capacity=parallel_model.capacity,
            section_id=parallel_model.section.id,
            school_year_id=parallel_model.schoolYear.id
        )

    def update(self, parallel):
        """Update an existing parallel."""
        parallel_model = ParallelModel.objects.get(id=parallel.id, deleted=False)
        parallel_model.name = parallel.name
        parallel_model.course_id = parallel.course_id
        parallel_model.capacity = parallel.capacity
        parallel_model.section_id = parallel.section_id
        parallel_model.schoolYear_id = parallel.school_year_id
        parallel_model.save()
        return Parallel(
            id=parallel_model.id,
            name=parallel_model.name,
            course_id=parallel_model.course.id,
            capacity=parallel_model.capacity,
            section_id=parallel_model.section.id,
            school_year_id=parallel_model.schoolYear.id
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
            course_id=parallel.course.id,
            capacity=parallel.capacity,
            section_id=parallel.section.id,
            school_year_id=parallel.schoolYear.id,
            course=course_model_to_entity(parallel.course),

            section=section_model_to_entity(parallel.section),

            school_year=school_year_model_to_entity(parallel.schoolYear)
        )

    def exists_by_name(self, name):
        """Check if a parallel exists by its name."""
        return ParallelModel.objects.filter(name=name, deleted=False).exists()

    def exist_by_course_id_and_section_id(self, course_id, section_id):
        """Check if a parallel exists by its course ID and section ID."""
        return ParallelModel.objects.filter(course_id=course_id, 
                                            section_id=section_id, 
                                            deleted=False).exists()
    
    def exist_by_id(self, parallel_id):
        """Check if a parallel exists by its ID."""
        return ParallelModel.objects.filter(id=parallel_id, deleted=False).exists()
    
    def exist_by_course_id_and_section_id_except_id(self, course_id, section_id, parallel_id):
        """Check if a parallel exists by its course ID and section ID except for a specific parallel ID."""
        return ParallelModel.objects.filter(course_id=course_id, 
                                            section_id=section_id, 
                                            deleted=False).exclude(id=parallel_id).exists()
        
    def find_by_course_id(self, course_id):
        """Find all parallels by course ID."""
        parallels = ParallelModel.objects.filter(course_id=course_id, deleted=False).order_by('id')
        
        return [ Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course.id,
            capacity=parallel.capacity,
            section_id=parallel.section.id,
            school_year_id=parallel.schoolYear.id,
            course=course_model_to_entity(parallel.course),

            section=section_model_to_entity(parallel.section),

            school_year=school_year_model_to_entity(parallel.schoolYear)
        
        ) for parallel in parallels]

    def find_by_filter(self, **filters):
        """
        Find parallels by the given filter.
        :param filter: The filter to apply.
        :return: A list of parallels matching the filter.
        """
        queryset = ParallelModel.objects.filter(deleted=False)
        queryset = queryset.filter(**filters).order_by('id')
        return [Parallel(
            id=parallel.id,
            name=parallel.name,
            course_id=parallel.course.id,
            capacity=parallel.capacity,
            section_id=parallel.section.id,
            school_year_id=parallel.schoolYear.id,
            course=course_model_to_entity(parallel.course),

            section=section_model_to_entity(parallel.section),

            school_year=school_year_model_to_entity(parallel.schoolYear)

        ) for parallel in queryset]
