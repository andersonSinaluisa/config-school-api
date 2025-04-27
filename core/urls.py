from rest_framework.routers import DefaultRouter

from core.api.views.course_views import CourseViewSet
from core.api.views.level_views import LevelViewSet
from core.api.views.subject_views import SubjectViewSet
from core.api.views.course_subject_view import CourseSubjectViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'levels', LevelViewSet, basename='level')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'course-subjects', CourseSubjectViewSet, basename='course-subject')
urlpatterns = router.urls
