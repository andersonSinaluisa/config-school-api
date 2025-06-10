from rest_framework.routers import DefaultRouter

from core.api.views.course_views import CourseViewSet
from core.api.views.level_views import LevelViewSet
from core.api.views.subject_views import SubjectViewSet
from core.api.views.course_subject_view import CourseSubjectAPIView, CourseSubjectViewSet
from core.api.views.parallel_views import ParallelViewSet
from core.api.views.school_year_views import SchoolYearViewSet
from core.api.views.section_view import SectionViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'levels', LevelViewSet, basename='levels')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'course-subjects', CourseSubjectViewSet, basename='course-subjects')
router.register(r'parallels', ParallelViewSet, basename='parallels')
router.register(r'school-years', SchoolYearViewSet, basename='school-years')
router.register(r'sections', SectionViewSet, basename='sections')



urlpatterns = [
    
    path('course-subjects/assing/<int:course_id>/', CourseSubjectAPIView.as_view(), name='course-subjects-assign'),
]
urlpatterns += router.urls