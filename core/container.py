# containers.py
from dependency_injector import containers, providers
from core.application.services.parallel.list_parallel_by_course_service import ListParallelByCourseService
from core.application.services.course_subjects.create_course_subject_service import CreateCourseSubjectService
from core.application.services.course_subjects.create_range_course_subject_service import CreateRangeCourseSubjectService
from core.application.services.course_subjects.delete_course_subject_service import DeleteCourseSubjectService
from core.application.services.course_subjects.get_course_subject_service import GetCourseSubjectService
from core.application.services.course_subjects.list_course_subject_service import ListCourseSubjectService
from core.application.services.course_subjects.remove_from_course_service import RemoveFromCourseService
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
from core.application.services.parallel.create_parallel_service import CreateParallelService
from core.application.services.parallel.delete_parallel_service import DeleteParallelService
from core.application.services.parallel.get_parallel_service import GetParallelService
from core.application.services.parallel.list_parallel_service import ListParallelService
from core.application.services.parallel.update_parallel_service import UpdateParallelService
from core.application.services.school_year.create_school_year_service import CreateSchoolYearService
from core.application.services.school_year.delete_school_year_service import DeleteSchoolYearService
from core.application.services.school_year.get_school_year_service import GetSchoolYearService
from core.application.services.school_year.list_school_year_service import ListSchoolYearService
from core.application.services.school_year.update_school_year_service import UpdateSchoolYearService
from core.application.services.sections.create_section_service import CreateSectionService
from core.application.services.sections.delete_section_service import DeleteSectionService
from core.application.services.sections.get_section_service import GetSectionService
from core.application.services.sections.list_section_service import ListSectionService
from core.application.services.sections.update_section_service import UpdateSectionService
from core.application.services.subjects.create_subject_service import CreateSubjectService
from core.application.services.subjects.delete_subject_service import DeleteSubjectService
from core.application.services.subjects.get_subject_service import GetSubjectService
from core.application.services.subjects.list_subject_service import ListSubjectService
from core.application.services.subjects.update_subject_service import UpdateSubjectService
from core.infrastructure.persistence.course_orm_adapter import CourseORMAdapter
from core.infrastructure.persistence.course_subject_orm_repository import CourseSubjectOrmRepository
from core.infrastructure.persistence.level_orm_repository import LevelOrmRepository
from core.infrastructure.persistence.parallel_orm_repository import ParallelORMRepository
from core.infrastructure.persistence.school_year_orm_repository import SchoolYearOrmRepository
from core.infrastructure.persistence.section_orm_repository import SectionOrmRepository
from core.infrastructure.persistence.subject_orm_repository import SubjectOrmRepository
from core.application.services.course_subjects.list_from_couse_service import ListFromCourseService
from core.application.services.course_subjects.remove_range_from_course import RemoveRangeFromCourse
class Container(containers.DeclarativeContainer):
    course_repository = providers.Singleton(CourseORMAdapter)
    level_repository = providers.Singleton(LevelOrmRepository)
    subject_repository = providers.Singleton(SubjectOrmRepository)
    course_subject_repository = providers.Singleton(CourseSubjectOrmRepository)
    list_parallel_respository = providers.Singleton(ParallelORMRepository)
    school_year_repository = providers.Singleton(SchoolYearOrmRepository)
    section_repository = providers.Singleton(SectionOrmRepository)
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
    
    list_subjects_from_course = providers.Factory(
        ListFromCourseService,
        course_subject_repository=course_subject_repository,
    )
    
    # CreateRangeCourseSubjectService
    create_range_course_subject_service = providers.Factory(
        CreateRangeCourseSubjectService,
        course_subject_repository=course_subject_repository,
    )
    
    # RemoveFromCourseService
    remove_from_course_service = providers.Factory(
        RemoveFromCourseService,
        course_subject_repository=course_subject_repository,
    )
    
    remove_range_from_course_service = providers.Factory(
        RemoveRangeFromCourse,
        course_subject_repository=course_subject_repository,
    )
    '''
    ==========
    Parallel Services
    ==========
    '''
    list_parallel_service = providers.Factory(
        ListParallelService,
        parallel_repository=list_parallel_respository,
    )
    list_parallel_by_course_service = providers.Factory(
        ListParallelByCourseService,
        parallel_repository=list_parallel_respository,
    )
    create_parallel_service = providers.Factory(
        CreateParallelService,
        parallel_repository=list_parallel_respository,
        course_repository=course_repository,
        section_repository=section_repository,
        school_year_repository=school_year_repository
    )
    
    update_parallel_service = providers.Factory(
        UpdateParallelService,
        parallel_repository=list_parallel_respository,
        course_repository=course_repository,
        section_repository=section_repository,
        school_year_repository=school_year_repository

    )
    
    
    delete_parallel_service = providers.Factory(
        DeleteParallelService,
        parallel_repository=list_parallel_respository,
    )
    
    get_parallel_service = providers.Factory(
        GetParallelService,
        parallel_repository=list_parallel_respository,
    )
    
    
    '''
    ==========
    School Year Services
    ==========
    '''
    
    create_school_year_service = providers.Factory(
        CreateSchoolYearService,
        school_year_repository=school_year_repository,
    )
    
    list_school_year_service = providers.Factory(
        ListSchoolYearService,
        school_year_repository=school_year_repository,
    )
    
    get_school_year_service = providers.Factory(
        GetSchoolYearService,
        school_year_repository=school_year_repository,
    )
    update_school_year_service = providers.Factory(
        UpdateSchoolYearService,
        school_year_repository=school_year_repository,
    )
    
    
    delete_school_year_service = providers.Factory(
        DeleteSchoolYearService,
        school_year_repository=school_year_repository,
    )
    
    '''
    ==========
    Section Services
    ==========
    '''
    
    list_section_service = providers.Factory(
        ListSectionService,
        section_repository=section_repository,
    )
    
    
    create_section_service = providers.Factory(
        CreateSectionService,
        section_repository=section_repository,
    )
    
    update_section_service = providers.Factory(
        UpdateSectionService,
        section_repository=section_repository,
    )
    
    delete_section_service = providers.Factory(
        DeleteSectionService,
        section_repository=section_repository,
    )
    
    get_section_service = providers.Factory(
        GetSectionService,
        section_repository=section_repository,
    )
    