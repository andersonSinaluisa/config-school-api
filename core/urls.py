from rest_framework.routers import DefaultRouter

from core.api.views.course_views import CourseViewSet
from core.api.views.level_views import LevelViewSet
from core.api.views.subject_views import SubjectViewSet
from core.api.views.course_subject_view import CourseSubjectAPIView, CourseSubjectViewSet
from core.api.views.parallel_views import ParallelViewSet
from core.api.views.school_year_views import SchoolYearViewSet
from core.api.views.section_view import SectionViewSet
from core.api.views.grading_system_views import GradingSystemViewSet
from core.api.views.grading_term_views import GradingTermViewSet
from core.api.views.evaluation_type_views import EvaluationTypeViewSet
from core.api.views.meeting_type_views import MeetingTypeViewSet
from core.api.views.attendance_code_views import AttendanceCodeViewSet
from core.api.views.behavior_scale_views import BehaviorScaleViewSet
from core.api.views.class_schedule_views import ClassScheduleViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'levels', LevelViewSet, basename='levels')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'course-subjects', CourseSubjectViewSet, basename='course-subjects')
router.register(r'parallels', ParallelViewSet, basename='parallels')
router.register(r'school-years', SchoolYearViewSet, basename='school-years')
router.register(r'sections', SectionViewSet, basename='sections')
router.register(r'grading-systems', GradingSystemViewSet, basename='grading-systems')
router.register(r'grading-terms', GradingTermViewSet, basename='grading-terms')
router.register(r'evaluation-types', EvaluationTypeViewSet, basename='evaluation-types')
router.register(r'meeting-types', MeetingTypeViewSet, basename='meeting-types')
router.register(r'attendance-codes', AttendanceCodeViewSet, basename='attendance-codes')
router.register(r'behavior-scales', BehaviorScaleViewSet, basename='behavior-scales')
router.register(r'class-schedules', ClassScheduleViewSet, basename='class-schedules')



urlpatterns = [

    path('course-subjects/assing/<int:course_id>/', CourseSubjectAPIView.as_view(), name='course-subjects-assign'),
]
urlpatterns += router.urls