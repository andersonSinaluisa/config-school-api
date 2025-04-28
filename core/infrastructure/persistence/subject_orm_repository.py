


from core.domain.entities.subject import Subject
from core.domain.repositories.subject_repository import SubjectRepository
from core.models import SubjectModel
from django.utils import timezone

class SubjectOrmRepository(SubjectRepository):
    """Subject ORM Adapter for interacting with the SubjectModel."""

    def get(self, subject_id: int):
        """Get a subject by its ID."""
        subject = SubjectModel.objects.get(id=subject_id, deleted=False)
        
        return Subject(
            id=subject.id,
            name=subject.name,
            description=subject.description,
            code=subject.code,
            hoursPerWeek=subject.hoursPerWeek
        )
        
    def all(self):
        """Get all subjects."""
        subjects = SubjectModel.objects.filter(deleted=False) .order_by('id')
        return [Subject(
            id=subject.id,
            name=subject.name,
            description=subject.description,
            code=subject.code,
            hoursPerWeek=subject.hoursPerWeek
        ) for subject in subjects]
        
    def create(self, subject: Subject):
        """Create a new subject."""
        subject_model = SubjectModel(
            name=subject.name,
            description=subject.description,
            code=subject.code,
            hoursPerWeek=subject.hoursPerWeek
        )
        subject_model.save()
        return Subject(
            id=subject_model.id,
            name=subject_model.name,
            description=subject_model.description,
            code=subject_model.code,
            hoursPerWeek=subject_model.hoursPerWeek
        )
        
    def update(self, subject):
        """Update an existing subject."""
        subject_model = SubjectModel.objects.get(id=subject.id)
        subject_model.name = subject.name
        subject_model.description = subject.description
        subject_model.code = subject.code
        subject_model.hoursPerWeek = subject.hoursPerWeek
        subject_model.save()
        return Subject(
            id=subject_model.id,
            name=subject_model.name,
            description=subject_model.description,
            code=subject_model.code,
            hoursPerWeek=subject_model.hoursPerWeek
        )
        
        
    def delete(self, subject_id: str):
        """Delete a subject by its ID."""
        subject_model = SubjectModel.objects.get(id=subject_id)
        subject_model.deleted = True
        subject_model.deleted_at = timezone.now()
        subject_model.save()
        return True
    
    def exist_by_name(self, name: str) -> bool:
        """Check if a subject exists by its name."""
        return SubjectModel.objects.filter(name=name, deleted=False).exists()
    
    
    def exist_by_id(self, subject_id: int) -> bool:
        """Check if a subject exists by its ID."""
        return SubjectModel.objects.filter(id=subject_id, deleted=False).exists()
    