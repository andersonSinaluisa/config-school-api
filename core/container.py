# containers.py
from dependency_injector import containers, providers
from core.application.services.course_subjects.create_course_subject_service import CreateCourseSubjectService
from core.application.services.course_subjects.delete_course_subject_service import DeleteCourseSubjectService
from core.application.services.course_subjects.get_course_subject_service import GetCourseSubjectService
from core.application.services.course_subjects.list_course_subject_service import ListCourseSubjectService
from core.application.services.course_subjects.update_course_subject_service import UpdateCourseSubjectService
from core.application.services.courses.create_course_service import CreateCourseService
from core.application.services.courses.delete_course_service import DeleteCourseService
from core.application.services.courses.get_course_service import GetCourseService
from core.application.services.courses.list_course_service import ListCourseService
from core.application.services.courses.update_course_service import UpdateCourseService
from core.application.services.levels.create_level_service import CreateLevelService
from core.application.services.levels.delete_level_service import DeleteLevelService
from core.application.services.levels.get_level_service import GetLevelService
from core.application.services.levels.list_level_service import ListLevelService
from core.application.services.levels.update_level_service import UpdateLevelService
from core.application.services.subjects.create_subject_service import CreateSubjectService
from core.application.services.subjects.delete_subject_service import DeleteSubjectService
from core.application.services.subjects.get_subject_service import GetSubjectService
from core.application.services.subjects.list_subject_service import ListSubjectService
from core.application.services.subjects.update_subject_service import UpdateSubjectService
from core.infrastructure.persistence.course_orm_adapter import CourseORMAdapter
from core.infrastructure.persistence.course_subject_orm_repository import CourseSubjectOrmRepository
from core.infrastructure.persistence.level_orm_repository import LevelOrmRepository
from core.infrastructure.persistence.subject_orm_repository import SubjectOrmRepository


class Container(containers.DeclarativeContainer):
    course_repository = providers.Singleton(CourseORMAdapter)
    level_repository = providers.Singleton(LevelOrmRepository)
    subject_repository = providers.Singleton(SubjectOrmRepository)
    course_subject_repository = providers.Singleton(CourseSubjectOrmRepository)
    '''
    ==========
    Course Services
    ==========
    '''
    create_course_service = providers.Factory(
        CreateCourseService,
        course_repository=course_repository,
        level_repository=level_repository,
    )
    list_course_service = providers.Factory(
        ListCourseService,
        course_repository=course_repository,
    )
    
    get_course_service = providers.Factory(
        GetCourseService,
        course_repository=course_repository,
    )
    
    delete_course_service = providers.Factory(
        DeleteCourseService,
        course_repository=course_repository,
    )
    update_course_service = providers.Factory(
        UpdateCourseService,
        course_repository=course_repository,
        level_repository=level_repository,
    )
    
    '''
    ==========
    Level Services
    ==========
    '''
    list_level_service = providers.Factory(
        ListLevelService,
        level_repository=level_repository,
    )
    get_level_service = providers.Factory(
        GetLevelService,
        level_repository=level_repository,
    )
    update_level_service = providers.Factory(
        UpdateLevelService,
        level_repository=level_repository,
    )
    delete_level_service = providers.Factory(
        DeleteLevelService,
        level_repository=level_repository,
    )
    create_level_service = providers.Factory(
        CreateLevelService,
        level_repository=level_repository,
    )
    
    '''
    ==========
    Subject Services
    ==========
    '''
    create_subject_service = providers.Factory(
        CreateSubjectService,
        subject_repository=subject_repository,
    )
    
    list_subject_service = providers.Factory(
        ListSubjectService,
        subject_repository=subject_repository,
    )
    
    get_subject_service = providers.Factory(
        GetSubjectService,
        subject_repository=subject_repository,
    )
    
    update_subject_service = providers.Factory(
        UpdateSubjectService,
        subject_repository=subject_repository,
    )
    
    delete_subject_service = providers.Factory(
        DeleteSubjectService,
        subject_repository=subject_repository,
    )
    
    '''
    ==========
    CourseSubject Services
    ==========
    '''
    
    create_course_subject_service = providers.Factory(
        CreateCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    
    list_course_subject_service = providers.Factory(
        ListCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    
    get_course_subject_service = providers.Factory(
        GetCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    
    update_course_subject_service = providers.Factory(
        UpdateCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    
    delete_course_subject_service = providers.Factory(
        DeleteCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    