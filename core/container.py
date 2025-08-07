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
from core.application.services.grading_systems.create_grading_system_service import CreateGradingSystemService
from core.application.services.grading_systems.delete_grading_system_service import DeleteGradingSystemService
from core.application.services.grading_systems.get_grading_system_service import GetGradingSystemService
from core.application.services.grading_systems.list_grading_system_service import ListGradingSystemService
from core.application.services.grading_systems.update_grading_system_service import UpdateGradingSystemService
from core.application.services.grading_terms.create_grading_term_service import CreateGradingTermService
from core.application.services.grading_terms.delete_grading_term_service import DeleteGradingTermService
from core.application.services.grading_terms.get_grading_term_service import GetGradingTermService
from core.application.services.grading_terms.list_grading_term_service import ListGradingTermService
from core.application.services.grading_terms.update_grading_term_service import UpdateGradingTermService
from core.application.services.evaluation_types.create_evaluation_type_service import CreateEvaluationTypeService
from core.application.services.evaluation_types.delete_evaluation_type_service import DeleteEvaluationTypeService
from core.application.services.evaluation_types.get_evaluation_type_service import GetEvaluationTypeService
from core.application.services.evaluation_types.list_evaluation_type_service import ListEvaluationTypeService
from core.application.services.evaluation_types.update_evaluation_type_service import UpdateEvaluationTypeService
from core.application.services.meeting_types.create_meeting_type_service import CreateMeetingTypeService
from core.application.services.meeting_types.delete_meeting_type_service import DeleteMeetingTypeService
from core.application.services.meeting_types.get_meeting_type_service import GetMeetingTypeService
from core.application.services.meeting_types.list_meeting_type_service import ListMeetingTypeService
from core.application.services.meeting_types.update_meeting_type_service import UpdateMeetingTypeService
from core.application.services.attendance_codes.create_attendance_code_service import CreateAttendanceCodeService
from core.application.services.attendance_codes.delete_attendance_code_service import DeleteAttendanceCodeService
from core.application.services.attendance_codes.get_attendance_code_service import GetAttendanceCodeService
from core.application.services.attendance_codes.list_attendance_code_service import ListAttendanceCodeService
from core.application.services.attendance_codes.update_attendance_code_service import UpdateAttendanceCodeService
from core.application.services.behavior_scales.create_behavior_scale_service import CreateBehaviorScaleService
from core.application.services.behavior_scales.delete_behavior_scale_service import DeleteBehaviorScaleService
from core.application.services.behavior_scales.get_behavior_scale_service import GetBehaviorScaleService
from core.application.services.behavior_scales.list_behavior_scale_service import ListBehaviorScaleService
from core.application.services.behavior_scales.update_behavior_scale_service import UpdateBehaviorScaleService
from core.application.services.class_schedules.create_class_schedule_service import CreateClassScheduleService
from core.application.services.class_schedules.list_class_schedule_service import ListClassScheduleService
from core.application.services.class_schedules.get_class_schedule_service import GetClassScheduleService
from core.application.services.class_schedules.update_class_schedule_service import UpdateClassScheduleService
from core.application.services.class_schedules.delete_class_schedule_service import DeleteClassScheduleService
from core.application.services.academic_plannings.create_academic_planning_service import CreateAcademicPlanningService
from core.application.services.academic_plannings.list_academic_planning_service import ListAcademicPlanningService
from core.application.services.academic_plannings.get_academic_planning_service import GetAcademicPlanningService
from core.application.services.academic_plannings.update_academic_planning_service import UpdateAcademicPlanningService
from core.application.services.academic_plannings.delete_academic_planning_service import DeleteAcademicPlanningService
from core.infrastructure.persistence.course_orm_adapter import CourseORMAdapter
from core.infrastructure.persistence.course_subject_orm_repository import CourseSubjectOrmRepository
from core.infrastructure.persistence.level_orm_repository import LevelOrmRepository
from core.infrastructure.persistence.parallel_orm_repository import ParallelORMRepository
from core.infrastructure.persistence.school_year_orm_repository import SchoolYearOrmRepository
from core.infrastructure.persistence.section_orm_repository import SectionOrmRepository
from core.infrastructure.persistence.subject_orm_repository import SubjectOrmRepository
from core.infrastructure.persistence.grading_system_orm_repository import GradingSystemOrmRepository
from core.infrastructure.persistence.grading_term_orm_repository import GradingTermOrmRepository
from core.infrastructure.persistence.evaluation_type_orm_repository import EvaluationTypeOrmRepository
from core.infrastructure.persistence.meeting_type_orm_repository import MeetingTypeOrmRepository
from core.infrastructure.persistence.attendance_code_orm_repository import AttendanceCodeOrmRepository
from core.infrastructure.persistence.behavior_scale_orm_repository import BehaviorScaleOrmRepository
from core.infrastructure.persistence.class_schedule_orm_repository import ClassScheduleOrmRepository
from core.infrastructure.persistence.academic_planning_orm_repository import AcademicPlanningOrmRepository
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
    grading_system_repository = providers.Singleton(GradingSystemOrmRepository)
    grading_term_repository = providers.Singleton(GradingTermOrmRepository)
    evaluation_type_repository = providers.Singleton(EvaluationTypeOrmRepository)
    meeting_type_repository = providers.Singleton(MeetingTypeOrmRepository)
    attendance_code_repository = providers.Singleton(AttendanceCodeOrmRepository)
    behavior_scale_repository = providers.Singleton(BehaviorScaleOrmRepository)
    class_schedule_repository = providers.Singleton(ClassScheduleOrmRepository)
    academic_planning_repository = providers.Singleton(AcademicPlanningOrmRepository)
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

    '''
    ==========
    Grading System Services
    ==========
    '''

    create_grading_system_service = providers.Factory(
        CreateGradingSystemService,
        grading_system_repository=grading_system_repository,
    )

    list_grading_system_service = providers.Factory(
        ListGradingSystemService,
        grading_system_repository=grading_system_repository,
    )

    get_grading_system_service = providers.Factory(
        GetGradingSystemService,
        grading_system_repository=grading_system_repository,
    )

    update_grading_system_service = providers.Factory(
        UpdateGradingSystemService,
        grading_system_repository=grading_system_repository,
    )

    delete_grading_system_service = providers.Factory(
        DeleteGradingSystemService,
        grading_system_repository=grading_system_repository,
    )

    '''
    ==========
    Grading Term Services
    ==========
    '''

    create_grading_term_service = providers.Factory(
        CreateGradingTermService,
        grading_term_repository=grading_term_repository,
    )

    list_grading_term_service = providers.Factory(
        ListGradingTermService,
        grading_term_repository=grading_term_repository,
    )

    get_grading_term_service = providers.Factory(
        GetGradingTermService,
        grading_term_repository=grading_term_repository,
    )

    update_grading_term_service = providers.Factory(
        UpdateGradingTermService,
        grading_term_repository=grading_term_repository,
    )

    delete_grading_term_service = providers.Factory(
        DeleteGradingTermService,
        grading_term_repository=grading_term_repository,
    )

    '''
    ==========
    Evaluation Type Services
    ==========
    '''

    create_evaluation_type_service = providers.Factory(
        CreateEvaluationTypeService,
        evaluation_type_repository=evaluation_type_repository,
    )

    list_evaluation_type_service = providers.Factory(
        ListEvaluationTypeService,
        evaluation_type_repository=evaluation_type_repository,
    )

    get_evaluation_type_service = providers.Factory(
        GetEvaluationTypeService,
        evaluation_type_repository=evaluation_type_repository,
    )

    update_evaluation_type_service = providers.Factory(
        UpdateEvaluationTypeService,
        evaluation_type_repository=evaluation_type_repository,
    )

    delete_evaluation_type_service = providers.Factory(
        DeleteEvaluationTypeService,
        evaluation_type_repository=evaluation_type_repository,
    )

    '''
    ==========
    Meeting Type Services
    ==========
    '''

    create_meeting_type_service = providers.Factory(
        CreateMeetingTypeService,
        meeting_type_repository=meeting_type_repository,
    )

    list_meeting_type_service = providers.Factory(
        ListMeetingTypeService,
        meeting_type_repository=meeting_type_repository,
    )

    get_meeting_type_service = providers.Factory(
        GetMeetingTypeService,
        meeting_type_repository=meeting_type_repository,
    )

    update_meeting_type_service = providers.Factory(
        UpdateMeetingTypeService,
        meeting_type_repository=meeting_type_repository,
    )

    delete_meeting_type_service = providers.Factory(
        DeleteMeetingTypeService,
        meeting_type_repository=meeting_type_repository,
    )

    '''
    ==========
    Attendance Code Services
    ==========
    '''

    create_attendance_code_service = providers.Factory(
        CreateAttendanceCodeService,
        attendance_code_repository=attendance_code_repository,
    )

    list_attendance_code_service = providers.Factory(
        ListAttendanceCodeService,
        attendance_code_repository=attendance_code_repository,
    )

    get_attendance_code_service = providers.Factory(
        GetAttendanceCodeService,
        attendance_code_repository=attendance_code_repository,
    )

    update_attendance_code_service = providers.Factory(
        UpdateAttendanceCodeService,
        attendance_code_repository=attendance_code_repository,
    )

    delete_attendance_code_service = providers.Factory(
        DeleteAttendanceCodeService,
        attendance_code_repository=attendance_code_repository,
    )

    '''
    ==========
    Behavior Scale Services
    ==========
    '''

    create_behavior_scale_service = providers.Factory(
        CreateBehaviorScaleService,
        behavior_scale_repository=behavior_scale_repository,
    )

    list_behavior_scale_service = providers.Factory(
        ListBehaviorScaleService,
        behavior_scale_repository=behavior_scale_repository,
    )

    get_behavior_scale_service = providers.Factory(
        GetBehaviorScaleService,
        behavior_scale_repository=behavior_scale_repository,
    )

    update_behavior_scale_service = providers.Factory(
        UpdateBehaviorScaleService,
        behavior_scale_repository=behavior_scale_repository,
    )

    delete_behavior_scale_service = providers.Factory(
        DeleteBehaviorScaleService,
        behavior_scale_repository=behavior_scale_repository,
    )

    '''
    ==========
    Class Schedule Services
    ==========
    '''

    create_class_schedule_service = providers.Factory(
        CreateClassScheduleService,
        class_schedule_repository=class_schedule_repository,
        course_repository=course_repository,
        parallel_repository=list_parallel_respository,
        school_year_repository=school_year_repository,
        subject_repository=subject_repository,
    )

    list_class_schedule_service = providers.Factory(
        ListClassScheduleService,
        class_schedule_repository=class_schedule_repository,
    )

    get_class_schedule_service = providers.Factory(
        GetClassScheduleService,
        class_schedule_repository=class_schedule_repository,
    )

    update_class_schedule_service = providers.Factory(
        UpdateClassScheduleService,
        class_schedule_repository=class_schedule_repository,
        course_repository=course_repository,
        parallel_repository=list_parallel_respository,
        school_year_repository=school_year_repository,
        subject_repository=subject_repository,
    )

    delete_class_schedule_service = providers.Factory(
        DeleteClassScheduleService,
        class_schedule_repository=class_schedule_repository,
    )

    '''
    ===========
    Academic Planning Services
    ===========
    '''

    create_academic_planning_service = providers.Factory(
        CreateAcademicPlanningService,
        academic_planning_repository=academic_planning_repository,
        course_repository=course_repository,
        parallel_repository=list_parallel_respository,
        school_year_repository=school_year_repository,
        subject_repository=subject_repository,
    )

    list_academic_planning_service = providers.Factory(
        ListAcademicPlanningService,
        academic_planning_repository=academic_planning_repository,
    )

    get_academic_planning_service = providers.Factory(
        GetAcademicPlanningService,
        academic_planning_repository=academic_planning_repository,
    )

    update_academic_planning_service = providers.Factory(
        UpdateAcademicPlanningService,
        academic_planning_repository=academic_planning_repository,
        course_repository=course_repository,
        parallel_repository=list_parallel_respository,
        school_year_repository=school_year_repository,
        subject_repository=subject_repository,
    )

    delete_academic_planning_service = providers.Factory(
        DeleteAcademicPlanningService,
        academic_planning_repository=academic_planning_repository,
    )
    