


from core.domain.repositories.parallel_repository import ParallelRepository


from typing import Optional


class ListParallelService:
    def __init__(self, parallel_repository: ParallelRepository):
        self.parallel_repository = parallel_repository

    def execute(
        self,
        *,
        course_id: Optional[str] = None,
        school_year_id: Optional[str] = None,
        name: Optional[str] = None,
        is_active: Optional[bool] = None,
    ):
        """
        Devuelve paralelos según filtros opcionales.
        Si no hay filtros, devuelve todos.
        """
        filters = {
            "course_id": course_id,
            "school_year_id": school_year_id,
            "name__icontains": name,      # ejemplo de búsqueda parcial
            "is_active": is_active,
        }
        # elimina None
        filters = {k: v for k, v in filters.items() if v is not None}
        return self.parallel_repository.find_by_filter(**filters)
